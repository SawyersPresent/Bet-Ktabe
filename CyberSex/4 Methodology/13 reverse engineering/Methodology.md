
# IDA free balling

## Gather basic info



## Strings

```
view -> view subviews -> strings
```

or 

```
Shift + f12
```



## examine sections / structure 


```
View → Open Subviews → Segments
```

or 

```
Shift + f7
```

**What to look for:**

- `.text` = Code (executable instructions)
- `.data` = Initialized global variables
- `.bss` = Uninitialized global variables
- `.rdata` = Read-only data (strings, constants)
- `.idata` = Import table (external functions)

**How to read this:**

```
.text:  0x0 - 0x1920 (6,432 bytes) r-x
        ↑ Start   ↑ End     ↑ Size    ↑ Permissions (read, execute)
```


## Finding entry points

**In IDA Pro:**

```
View → Open Subviews → Exports
Or press: Shift+F4
```

**For this COFF file, I found 14 functions:**

```
getDllAddr                (0x0)
append_to_buffer          (0x2d)
int_to_string             (0x118)
escape_json_string        (0x1d5)
send_json_base_data       (0x25b)
frequency_to_channel      (0x667)
send_json_monitor_data    (0x6c7)
convert_dbm_to_decimal    (0xb44)
display_base_signal       (0xb64)
calculate_real_snr        (0xc91)
base                      (0xcb9)
collect_wifi_signal_str.. (0x1187)
display_signal_samples    (0x14a9)
go                        (0x1597)
```

**Pro Tip #3:** Function names reveal architecture:

- `go()` is a common BOF entry point name
- `send_json_*` = data exfiltration functions
- `display_*` = output/UI functions
- `collect_*` = core functionality
- Helper functions like `int_to_string` = utility code

**Mental model to build:**

```
Entry Point (go)
    ├── Mode Selection Logic
    ├── base() ──────────► collect samples ──► display_base_signal()
    │                                       └─► send_json_base_data()
    └── monitor mode ────► collect_wifi_signal_strength()
                        └─► display_signal_samples()
                        └─► send_json_monitor_data()
```



# Finding imports

## Map External Dependencies (What Does It Need?)

### Examine Imports


```
View → Open Subviews → Imports
Or press: Ctrl+F5
```

If not then it might be in the names view

```
View → Open Subviews → Names
```

### Check the UNDEF Segment

```
View → Open Subviews → Segments
Double-click on "UNDEF" segment
```

The UNDEF section contains **external symbols** - things defined elsewhere:

```
UNDEF segment:
  __imp_LoadLibraryA
  __imp_GetProcAddress  
  __imp_MSVCRT$strlen
  __imp_KERNEL32$GetProcessHeap
  ... etc ...
```

**These are your "imports"!** Just not in a traditional import table.


# Understanding the functions

#### Example 1: `frequency_to_channel()`

**Step 1 - Read the name:** Converts frequency to WiFi channel number

**Step 2 - Check size:** 96 bytes = small, probably simple math

**Step 3 - Decompile:**

```c
int frequency_to_channel(int freq_khz) {
  if (freq_khz == 2484000)
    return 14;  // Special case: Channel 14 (Japan)
  
  if (freq_khz >= 2412000 && freq_khz <= 2472000)
    return (freq_khz - 2412000) / 5000 + 1;  // 2.4 GHz band
  
  if (freq_khz >= 5170000 && freq_khz <= 5825000)
    return (freq_khz - 5170000) / 5000 + 34;  // 5 GHz band
  
  return 0;  // Unknown
}
```

**Verify logic with known values:

```
Channel 1 = 2412 MHz
Calculation: (2412000 - 2412000) / 5000 + 1 = 0 + 1 = 1 ✓

Channel 6 = 2437 MHz  
Calculation: (2437000 - 2412000) / 5000 + 1 = 5 + 1 = 6 ✓

Makes sense! This is the standard WiFi channel formula.
```

#### Example 2: `calculate_real_snr()`


```c
int calculate_real_snr(int signal_dbm, int noise_dbm) {
  return signal_dbm - noise_dbm;
}
```

**This is correct!** SNR in dB = Signal - Noise (both in dBm)
























