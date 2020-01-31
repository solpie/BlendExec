import Vue from "vue";
import ElementUI from "element-ui";
import '../theme/index.css'
import App from "./App.vue";
import { Button, Select, Menu, MenuItem, MenuItemGroup } from "element-ui";
import axios from "axios";

Vue.prototype.$http = axios;
Vue.prototype.$eventHub = new Vue(); 
window.onresize = (v) => {
  Vue.prototype.$eventHub.$emit('win_resize',v)
}
window.onkeydown = (e) => {
  Vue.prototype.$eventHub.$emit('win_keydown',e)
}
window.onkeyup = (e) => {
  Vue.prototype.$eventHub.$emit('win_keyup',e)
}
Vue.use(ElementUI);
Vue.use(Select);
Vue.use(Button);
Vue.use(Menu);
Vue.use(MenuItem);
Vue.use(MenuItemGroup);
new Vue({
  el: "#app",
  render: h => h(App)
});
