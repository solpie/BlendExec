import Vue from "vue";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import App from "./App.vue";
import { Button, Select, Menu, MenuItem, MenuItemGroup } from "element-ui";

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
