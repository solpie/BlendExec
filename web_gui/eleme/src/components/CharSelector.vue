<template>
  <div>
    <el-tabs
      v-if="bone_map"
      tab-position="right"
      style="height: 600px;position:relative"
    >
      <el-tab-pane
        v-for="(item, n1) in bone_map"
        :key="n1"
        :label="item.tab"
        style="height:600px;border: 1px solid #eee"
      >
        <el-image
          v-if="item.bg"
          style="width: 100%;"
          :src="item.bg"
          fit="contain"
          disabled
          id="map_bg"
          @load="on_map_bg_loaded"
          @click="on_create_node($event, item)"
        />
        <div :style="zoom_style">
          <el-radio
            draggable="true"
            v-for="(node, i) in item.node"
            :key="i"
            :id="node.bone_name"
            v-model="bone"
            :label="node.bone_name"
            :style="node.style"
            @change="on_sel_node(node)"
            >{{ node.bone_name }}
            {{ node.style.left + node.style.top }}</el-radio
          >
        </div>
        <el-collapse v-model="activeNames">
          <el-collapse-item title="node editor" name="1">
            <el-row>
              <el-col :span="12">
                <el-input
                  size="mini"
                  v-model="item.rig_object_name"
                  :maxlength="20"
                >
                  <template slot="prepend">rig object name</template>
                </el-input>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span="12">
                <el-input
                  size="mini"
                  v-model="bone"
                  @change="on_edit_bone_name"
                >
                  <template slot="prepend">bone name</template>
                </el-input>
              </el-col>
              <el-col :span="12">
                <el-button size="mini" @click="on_add_node(item)"
                  >Add</el-button
                >
                <el-button size="mini" @click="on_del_node">Del</el-button>
                <el-button size="mini" @click="on_edit">Edit</el-button>
                <el-button size="mini" @click="on_save">Save</el-button>
              </el-col>
            </el-row>
          </el-collapse-item>
        </el-collapse>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
import { api } from "@/api/v1.js";
import { dragElement } from "@/utils/drag.js";
export default {
  name: "CharSelector",
  data() {
    return {
      bone: "",
      new_count: 1,
      last_sel_node: null,
      activeNames: ["0"],
      zoom_style:{
          position:"absolute",
          top:"0px",
          zoom: 1.14
      },
      is_edit_mode: false,
      bone_map: null,
      config: null,
      config_fly: { scale: 1 }
    };
  },
  props: {
    msg: String
  },
  mounted() {
    this.init_ui();
  },
  methods: {
    on_del_node() {
      for (let item of this.bone_map) {
        let a = [];
        for (let node of item.node) {
          if (node.bone_name === this.last_sel_node.bone_name) {
            continue;
          } else {
            a.push(node);
          }
        }
        item.node = a;
      }
    },
    on_create_node(event, item) {
      let map = document.getElementById("map_bg");
      let scale = map.clientWidth / item.width;
      this.config_fly.scale = scale;
      console.log(
        "on_create_node",
        map.clientWidth,
        scale,
        event.target.x,
        event.target.y
      );
      console.log("on_create_node", event, item.tab);
      this.on_map_bg_loaded();
    },
    on_edit_bone_name() {
      this.last_sel_node.bone_name = this.bone;
      console.log(this.bone, this.last_sel_node.bone_name);
    },
    async on_sel_node(node) {
      if (this.activeNames.length === 1 && this.activeNames[0] === "0") {
        //    api.run_bpy(api.hwnd, item.path);
        let bpy = api.bpy_sel_bone("rig", node.bone_name);
        console.log(bpy);
        let res = await api.run_bpy_str(bpy);
      }
      console.log(this.activeNames, node.bone_name);
      this.last_sel_node = node;
    },
    on_add_node(item) {
      let new_node = {
        name: "",
        bone_name: "bone_" + this.new_count,
        style: { left: "0px", top: "0px" }
      };
      item.node.push(new_node);
      this.new_count++;
    },
    on_edit() {
      for (let item of this.bone_map) {
        for (let node of item.node) {
          dragElement(document.getElementById(node.bone_name));
        }
      }
    },
    async on_save() {
      let _ = (elem, prop, parent_ofs, scale) => {
        let x = Number(elem.style[prop].replace("px", "")) + parent_ofs;
        let a = Math.floor(x / scale);
        return a;
      };
      let map = document.getElementById("map_bg");
      for (let item of this.bone_map) {
        let scale = map.clientWidth / item.width;
        if (scale) {
          let rect = map.getBoundingClientRect();
          for (let node of item.node) {
            let elem = document.getElementById(node.bone_name);
            console.log("before", elem.style.left);
            node.x = _(elem, "left", 0, 1);
            node.y = _(elem, "top", 0, 1);
            //   node.style.left = _(elem, "left");
            //   node.style.top = _(elem, "top");

            //   console.log("fixed", elem.style.left);
            //   node.style.left = Number(elem.style.left) / this.config_fly.scale;
            //   node.style.top = elem.style.top / this.config_fly.scale;
          }
        }
      }
      let res = await api.save_bone_map(this.config);
    },
    on_map_bg_loaded() {
      console.log("on_map_bg_loaded");
      let _ = (node, src_prop, prop, scale, ofs) => {
        let src_n = node[src_prop];

        let a = Math.floor(node[src_prop] * scale);
        node.style[prop] = a + "px";
        console.log("src", src_n, a);
      };
      let map = document.getElementById("map_bg");

      for (let item of this.bone_map) {
        let scale = map.clientWidth / item.width;
        let rect = map.getBoundingClientRect();
        console.log(item.tab, "scale", scale);
        if (scale)
        {
            this.zoom_style.zoom = scale
            for (let node of item.node) {
              _(node, "x", "left", 1, rect.x);
              _(node, "y", "top", 1, 0);
            }
        }
      }
    },
    async init_ui() {
      let config = await api.get("/static/config.json");
      this.config = config;
      this.bone_map = config.map;
      console.log(api, config);
    }
  }
};
</script>
