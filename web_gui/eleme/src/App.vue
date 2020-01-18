<template>
  <div id="app">
    <el-container style="border: 1px solid #eee">
      <el-header>
        <NavMenu />
      </el-header>
      <el-container>
        <el-aside>
          <BpyShelf />
        </el-aside>
        <el-main>
          <HelloWorld msg="Welcome to Your Vue.js App" />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import NavMenu from "./components/NavMenu.vue";
import BpyShelf from "./components/BpyShelf";
export default {
  name: "app",
  components: {
    BpyShelf,
    HelloWorld,
    NavMenu
  },
  data() {
    return {
      bpy_script_arr: ["1", "2"]
    };
  }
};
</script>
<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
