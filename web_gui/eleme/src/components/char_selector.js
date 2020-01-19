import { api } from "@/api/v1.js";
import { dragElement } from "@/utils/drag.js";
export default {
  name: "CharSelector",
  data() {
    return {
      bone: "",
      new_count: 1,
      map_src_width: 0,
      last_sel_node: null,
      activeNames: ["0"],
      zoom_style: {
        position: "absolute",
        top: "0px",
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
  watch: {
    // map_ctn_width: v => {
    //   // console.log("resize2", v);
    // }
  },
  mounted() {
    this.$eventHub.$on("win_resize", e => {
      this.update_map_zoom();
    });
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
    update_map_zoom() {
      let map = document.getElementById("map_bg");
      if (map) {
        let scale = map.clientWidth / this.map_src_width;
        this.zoom_style.zoom = scale;
      }
    },
    on_create_node(event, item) {
      let map = document.getElementById("map_bg");
      let rect = map.getBoundingClientRect();
      let node_x = event.clientX - rect.x;
      let node_y = event.clientY - rect.y;
      node_x = node_x * this.zoom_style.zoom;
      node_y = node_y * this.zoom_style.zoom;
      console.log("on_create_node", node_x, node_y, event, item.tab);
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
      let map = document.getElementById("map_bg");
      for (let item of this.bone_map) {
        let scale = map.clientWidth / item.width;
        if (scale) {
          let rect = map.getBoundingClientRect();
          for (let node of item.node) {
            let elem = document.getElementById(node.bone_name);
            console.log("before", elem.style.left);
              node.style.left = elem.style.left
              node.style.top = elem.style.top
          }
        }
      }
      let res = await api.save_bone_map(this.config);
    },
    on_resize() {
      console.log("on_resize");
    },
    on_map_bg_loaded() {
      console.log("on_map_bg_loaded");
      let _ = (node, src_prop, prop, scale, ofs) => {
        let src_n = node[src_prop];

        let a = Math.floor(node[src_prop] * scale)+ofs;
        node.style[prop] = a + "px";
        console.log("src", src_n, a);
      };
      let map = document.getElementById("map_bg");

      for (let item of this.bone_map) {
        let scale = map.clientWidth / item.width;
        let rect = map.getBoundingClientRect();
        console.log(item.tab, "scale", scale);
        if (scale) {
          this.zoom_style.zoom = scale;
          this.map_src_width = item.width;
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
