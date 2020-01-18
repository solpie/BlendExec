<template>
  <div id="app">
    <el-container >
      <el-header>
        <NavMenu />
      </el-header>
      <el-container >
        <el-aside style="border: 1px solid #eee">
          <BpyShelf />
        </el-aside>
        <el-main>
          <CharSelector msg="Welcome to Your Vue.js App" />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import NavMenu from "./components/NavMenu.vue";
import BpyShelf from "./components/BpyShelf";
import CharSelector from "./components/CharSelector";
export default {
  name: "app",
  components: {
    BpyShelf,
    CharSelector,
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
}
</style>
