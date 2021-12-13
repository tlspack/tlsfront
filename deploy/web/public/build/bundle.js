var app=function(){"use strict";function t(){}function n(t){return t()}function e(){return Object.create(null)}function r(t){t.forEach(n)}function c(t){return"function"==typeof t}function s(t,n){return t!=t?n==n:t!==n||t&&"object"==typeof t||"function"==typeof t}function o(t,n){t.appendChild(n)}function a(t,n,e){t.insertBefore(n,e||null)}function i(t){t.parentNode.removeChild(t)}function u(t){return document.createElement(t)}function l(t){return document.createTextNode(t)}function d(){return l(" ")}function f(t,n,e,r){return t.addEventListener(n,e,r),()=>t.removeEventListener(n,e,r)}function h(t,n,e){null==e?t.removeAttribute(n):t.getAttribute(n)!==e&&t.setAttribute(n,e)}function p(t,n){n=""+n,t.wholeText!==n&&(t.data=n)}function b(t,n,e){t.classList[e?"add":"remove"](n)}let m;function g(t){m=t}function $(t){(function(){if(!m)throw new Error("Function called outside component initialization");return m})().$$.on_mount.push(t)}const v=[],w=[],_=[],x=[],y=Promise.resolve();let S=!1;function A(t){_.push(t)}let C=!1;const T=new Set;function k(){if(!C){C=!0;do{for(let t=0;t<v.length;t+=1){const n=v[t];g(n),E(n.$$)}for(g(null),v.length=0;w.length;)w.pop()();for(let t=0;t<_.length;t+=1){const n=_[t];T.has(n)||(T.add(n),n())}_.length=0}while(v.length);for(;x.length;)x.pop()();S=!1,C=!1,T.clear()}}function E(t){if(null!==t.fragment){t.update(),r(t.before_update);const n=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,n),t.after_update.forEach(A)}}const L=new Set;function I(t,n){t&&t.i&&(L.delete(t),t.i(n))}function M(t,n,e,r){if(t&&t.o){if(L.has(t))return;L.add(t),undefined.c.push((()=>{L.delete(t),r&&(e&&t.d(1),r())})),t.o(n)}}function j(t){t&&t.c()}function O(t,e,s,o){const{fragment:a,on_mount:i,on_destroy:u,after_update:l}=t.$$;a&&a.m(e,s),o||A((()=>{const e=i.map(n).filter(c);u?u.push(...e):r(e),t.$$.on_mount=[]})),l.forEach(A)}function H(t,n){const e=t.$$;null!==e.fragment&&(r(e.on_destroy),e.fragment&&e.fragment.d(n),e.on_destroy=e.fragment=null,e.ctx=[])}function N(t,n){-1===t.$$.dirty[0]&&(v.push(t),S||(S=!0,y.then(k)),t.$$.dirty.fill(0)),t.$$.dirty[n/31|0]|=1<<n%31}function z(n,c,s,o,a,u,l,d=[-1]){const f=m;g(n);const h=n.$$={fragment:null,ctx:null,props:u,update:t,not_equal:a,bound:e(),on_mount:[],on_destroy:[],on_disconnect:[],before_update:[],after_update:[],context:new Map(c.context||(f?f.$$.context:[])),callbacks:e(),dirty:d,skip_bound:!1,root:c.target||f.$$.root};l&&l(h.root);let p=!1;if(h.ctx=s?s(n,c.props||{},((t,e,...r)=>{const c=r.length?r[0]:e;return h.ctx&&a(h.ctx[t],h.ctx[t]=c)&&(!h.skip_bound&&h.bound[t]&&h.bound[t](c),p&&N(n,t)),e})):[],h.update(),p=!0,r(h.before_update),h.fragment=!!o&&o(h.ctx),c.target){if(c.hydrate){const t=function(t){return Array.from(t.childNodes)}(c.target);h.fragment&&h.fragment.l(t),t.forEach(i)}else h.fragment&&h.fragment.c();c.intro&&I(n.$$.fragment),O(n,c.target,c.anchor,c.customElement),k()}g(f)}class F{$destroy(){H(this,1),this.$destroy=t}$on(t,n){const e=this.$$.callbacks[t]||(this.$$.callbacks[t]=[]);return e.push(n),()=>{const t=e.indexOf(n);-1!==t&&e.splice(t,1)}}$set(t){var n;this.$$set&&(n=t,0!==Object.keys(n).length)&&(this.$$.skip_bound=!0,this.$$set(t),this.$$.skip_bound=!1)}}function q(n){let e,c,s,l,p,m,g,$,v;return{c(){e=u("nav"),c=u("div"),s=u("a"),s.innerHTML='<img src="/assets/gigamon.png" width="32" height="32"/>\n\t\t\t    \n\t\t\t[ FM ]',l=d(),p=u("a"),p.innerHTML='<span aria-hidden="true"></span> \n\t\t\t<span aria-hidden="true"></span> \n\t\t\t<span aria-hidden="true"></span>',m=d(),g=u("div"),g.innerHTML='<div class="navbar-start"></div> \n\n\t\t<div class="navbar-end"><div class="navbar-item"></div></div>',h(s,"class","navbar-item"),h(s,"href","https://www.gigamon.com"),h(p,"role","button"),h(p,"class","navbar-burger"),h(p,"aria-label","menu"),h(p,"aria-expanded","false"),h(p,"data-target","navbarTopMenu"),h(c,"class","navbar-brand"),h(g,"id","navbarTopMenu"),h(g,"class","navbar-menu"),b(g,"is-active",n[0]),h(e,"class","navbar is-dark has-shadow"),h(e,"role","navigation"),h(e,"aria-label","main navigation")},m(t,r){a(t,e,r),o(e,c),o(c,s),o(c,l),o(c,p),o(e,m),o(e,g),$||(v=[f(window,"resize",n[1]),f(p,"click",n[2])],$=!0)},p(t,[n]){1&n&&b(g,"is-active",t[0])},i:t,o:t,d(t){t&&i(e),$=!1,r(v)}}}function B(t,n,e){let r=!1;return[r,()=>e(0,r=!1),()=>e(0,r=!r)]}class P extends F{constructor(t){super(),z(this,t,B,q,s,{})}}function D(t,n,e){const r=t.slice();return r[1]=n[e][0],r[2]=n[e][1],r}function G(t){let n,e,r,c,s,f,h,b,m,g,$,v,w,_,x,y,S,A,C,T,k,E=t[1]+"",L=t[2].sum.tcpAcceptSuccess+"",I=t[2].sum.sslAcceptSuccess+"",M=t[2].sum.tcpConnInitSuccess+"",j=t[2].sum.sslConnInitSuccess+"",O=t[2].sum.tcpActiveConns+"";return{c(){n=u("tr"),e=u("td"),r=l(E),c=d(),s=u("td"),f=l(L),h=d(),b=u("td"),m=l(I),g=d(),$=u("td"),v=l(M),w=d(),_=u("td"),x=l(j),y=d(),S=u("td"),A=l(O),C=d(),T=u("td"),T.textContent="show",k=d()},m(t,i){a(t,n,i),o(n,e),o(e,r),o(n,c),o(n,s),o(s,f),o(n,h),o(n,b),o(b,m),o(n,g),o(n,$),o($,v),o(n,w),o(n,_),o(_,x),o(n,y),o(n,S),o(S,A),o(n,C),o(n,T),o(n,k)},p(t,n){1&n&&E!==(E=t[1]+"")&&p(r,E),1&n&&L!==(L=t[2].sum.tcpAcceptSuccess+"")&&p(f,L),1&n&&I!==(I=t[2].sum.sslAcceptSuccess+"")&&p(m,I),1&n&&M!==(M=t[2].sum.tcpConnInitSuccess+"")&&p(v,M),1&n&&j!==(j=t[2].sum.sslConnInitSuccess+"")&&p(x,j),1&n&&O!==(O=t[2].sum.tcpActiveConns+"")&&p(A,O)},d(t){t&&i(n)}}}function J(n){let e,r,c,s,l=Object.entries(n[0]),f=[];for(let t=0;t<l.length;t+=1)f[t]=G(D(n,l,t));return{c(){e=u("table"),r=u("thead"),r.innerHTML='<tr><th class="svc_name svelte-1k8ujs0"><abbr title="ServiceName">Services</abbr></th> \n\n            <th><abbr title="tcpAcceptSuccess">TcpAccpt</abbr></th> \n            <th><abbr title="sslAcceptSuccess">SSLAccpt</abbr></th> \n\n            <th><abbr title="tcpConnInitSuccess">TcpConn</abbr></th> \n            <th><abbr title="sslConnInitSuccess">SSLConn</abbr></th> \n\n            <th><abbr title="tcpActiveConns">ActConn</abbr></th> \n\n            <th><abbr title="Throughput">Thpt</abbr></th></tr>',c=d(),s=u("tbody");for(let t=0;t<f.length;t+=1)f[t].c();h(e,"class","table is-bordered is-striped is-narrow is-hoverable is-fullwidth has-text-left")},m(t,n){a(t,e,n),o(e,r),o(e,c),o(e,s);for(let t=0;t<f.length;t+=1)f[t].m(s,null)},p(t,[n]){if(1&n){let e;for(l=Object.entries(t[0]),e=0;e<l.length;e+=1){const r=D(t,l,e);f[e]?f[e].p(r,n):(f[e]=G(r),f[e].c(),f[e].m(s,null))}for(;e<f.length;e+=1)f[e].d(1);f.length=l.length}},i:t,o:t,d(t){t&&i(e),function(t,n){for(let e=0;e<t.length;e+=1)t[e]&&t[e].d(n)}(f,t)}}}function K(t,n,e){let r={};return $((()=>{const t=setInterval((()=>{fetch("api/stats").then((t=>t.json())).then((t=>{e(0,r=t)}))}),1e3);return()=>{clearInterval(t)}})),[r]}class Q extends F{constructor(t){super(),z(this,t,K,J,s,{})}}function R(n){let e,r,c,s,l,f,p,b;return e=new P({}),p=new Q({}),{c(){j(e.$$.fragment),r=d(),c=u("div"),s=u("div"),l=u("div"),f=u("div"),j(p.$$.fragment),h(f,"class","container"),h(l,"class","column"),h(s,"class","columns"),h(c,"class","container")},m(t,n){O(e,t,n),a(t,r,n),a(t,c,n),o(c,s),o(s,l),o(l,f),O(p,f,null),b=!0},p:t,i(t){b||(I(e.$$.fragment,t),I(p.$$.fragment,t),b=!0)},o(t){M(e.$$.fragment,t),M(p.$$.fragment,t),b=!1},d(t){H(e,t),t&&i(r),t&&i(c),H(p)}}}return new class extends F{constructor(t){super(),z(this,t,null,R,s,{})}}({target:document.body,props:{name:"world"}})}();
//# sourceMappingURL=bundle.js.map
