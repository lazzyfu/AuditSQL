(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3e088796"],{"241ce":function(e,t,n){},"33e2":function(e,t,n){"use strict";var i=n("241ce"),a=n.n(i);a.a},"432b":function(e,t,n){"use strict";n.d(t,"a",(function(){return o}));var i=n("5530"),a=n("5880"),o={computed:Object(i["a"])(Object(i["a"])({},Object(a["mapState"])({layout:function(e){return e.app.layout},navTheme:function(e){return e.app.theme},primaryColor:function(e){return e.app.color},colorWeak:function(e){return e.app.weak},fixedHeader:function(e){return e.app.fixedHeader},fixedSidebar:function(e){return e.app.fixedSidebar},contentWidth:function(e){return e.app.contentWidth},autoHideHeader:function(e){return e.app.autoHideHeader},isMobile:function(e){return e.app.isMobile},sideCollapsed:function(e){return e.app.sideCollapsed},multiTab:function(e){return e.app.multiTab}})),{},{isTopMenu:function(){return"topmenu"===this.layout}}),methods:{isSideMenu:function(){return!this.isTopMenu}}}},cd07:function(e,t,n){"use strict";n.r(t);var i=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"page-header-index-wide"},[n("a-card",{style:{height:"100%"},attrs:{bordered:!1,bodyStyle:{padding:"16px 0",height:"100%"}}},[n("div",{staticClass:"account-settings-info-main",class:{mobile:e.isMobile}},[n("div",{staticClass:"account-settings-info-left"},[n("a-menu",{style:{border:"0",width:e.isMobile?"560px":"auto"},attrs:{mode:e.isMobile?"horizontal":"inline",selectedKeys:e.selectedKeys,type:"inner"},on:{openChange:e.onOpenChange}},[n("a-menu-item",{key:"/account/settings/base"},[n("router-link",{attrs:{to:{name:"BaseSettings"}}},[e._v(" 基本设置 ")])],1),n("a-menu-item",{key:"/account/settings/security"},[n("router-link",{attrs:{to:{name:"SecuritySettings"}}},[e._v(" 安全设置 ")])],1)],1)],1),n("div",{staticClass:"account-settings-info-right"},[n("div",{staticClass:"account-settings-info-title"},[n("span",[e._v(e._s(e.$route.meta.title))])]),n("route-view")],1)])])],1)},a=[],o=(n("99af"),n("680a")),u=n("432b"),s={components:{RouteView:o["b"]},mixins:[u["a"]],data:function(){return{mode:"inline",openKeys:[],selectedKeys:[],preview:{},option:{img:"/avatar2.jpg",info:!0,size:1,outputType:"jpeg",canScale:!1,autoCrop:!0,autoCropWidth:180,autoCropHeight:180,fixedBox:!0,fixed:!0,fixedNumber:[1,1]},pageTitle:""}},mounted:function(){this.updateMenu()},methods:{onOpenChange:function(e){this.openKeys=e},updateMenu:function(){var e=this.$route.matched.concat();this.selectedKeys=[e.pop().path]}},watch:{$route:function(e){this.updateMenu()}}},r=s,c=(n("33e2"),n("2877")),p=Object(c["a"])(r,i,a,!1,null,"6cb734a6",null);t["default"]=p.exports}}]);