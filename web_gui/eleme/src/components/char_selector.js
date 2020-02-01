import { api } from "@/api/v1.js";
import { dragElement } from "@/utils/drag.js";
import Poselib from "./Poselib";

function px_n(p) {
  return Number(p.replace("px", ""));
}
export default {
  name: "CharSelector",
  components: {
    Poselib
  },
  // watch: {

  // },
  data() {
    return {
      bone: "",
      map_src_width: 0,
      last_sel_node: null,
      is_edit_bone: false,
      rig_object_name: "",
      activeNames: ["0"],
      is_show_poselib: false,
      sel_tab: "",
      is_altKey: false,
      zoom_style: {
        position: "absolute",
        top: "0px",
        zoom: 1.14
      },
      bone_editor_style: {
        position: "absolute",
        left: "0px",
        "z-index": 9999,
        width: "200px",
        top: "0px"
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
    this.$eventHub.$on("win_keydown", e => {
      this.is_altKey = e.altKey;
    });
    this.$eventHub.$on("win_keyup", e => {
      // this.is_altKey = e.altKey;
      console.log(e);
      if (e.key === "e") {
        if (this.bone != "") {
          this.is_edit_bone = true;
        }
      } else if (e.key == "g") {
        this.is_edit_bone = false;
        this.on_edit();
      }
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
    attach_bone_editor(new_node) {
      this.bone_editor_style.left = new_node.style.left;
      this.bone_editor_style.top = new_node.style.top;
    },
    on_create_node(event, item) {
      let map = document.getElementById("map_bg");
      let rect = map.getBoundingClientRect();
      let node_x = event.clientX - rect.x;
      let node_y = event.clientY - rect.y;
      node_x = Math.floor(node_x / this.zoom_style.zoom);
      node_y = Math.floor(node_y / this.zoom_style.zoom);
      if (event.ctrlKey) {
        this.is_edit_bone = true;
        let new_node = {
          name: "",
          bone_name: "bone_" + (item.node.length + 1),
          style: { left: node_x + "px", top: node_y + "px" }
        };
        item.node.push(new_node);
        this.attach_bone_editor(new_node);
        this.bone = new_node.bone_name;
        this.last_sel_node = new_node;
      }
      console.log("on_create_node", node_x, node_y, event, item.tab);
    },
    on_mirror_bone(item) {
      // let mirror = ()
      let a = [];
      for (let node of item.node) {
        if (node.bone_name.search(".r") > -1) {
          let node_x = item.width - px_n(node.style.left);
          let new_node = {
            name: "",
            bone_name: node.bone_name.replace(".r", ".l"),
            style: { left: node_x + "px", top: node.style.top }
          };
          console.log("mirror node", new_node.bone_name);
          a.push(new_node);
        }
      }
      item.node = item.node.concat(a);
      console.log("on_mirror_bone", item.tab);
    },
    on_edit_bone_name() {
      this.last_sel_node.bone_name = this.bone;
      console.log(this.bone, this.last_sel_node.bone_name);
      this.bone = "";
      this.is_edit_bone = false;
    },
    on_tab_changed(e) {
      console.log("tab change", this.sel_tab);
      let tab_data = this.bone_map[this.sel_tab];
      if (tab_data.type === "pose") {
        this.is_show_poselib = true;
      }
    },
    async on_sel_node(e, node) {
      // let is_alt = this.is_altKey;
      if (!this.is_edit_mode) {
        let bpy = api.bpy_sel_bone("rig", node.bone_name);
        let res = await api.run_bpy_str(bpy);
        api.send_key("r");
      } else {
        this.attach_bone_editor(node);
        // this.is_edit_bone = true;
      }
      console.log(e, this.activeNames, node.bone_name);
      this.last_sel_node = node;
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
        // item.type = 'bone'
        let scale = map.clientWidth / item.width;
        if (scale) {
          let rect = map.getBoundingClientRect();
          for (let node of item.node) {
            let elem = document.getElementById(node.bone_name);
            console.log("before", elem.style.left);
            node.style.left = elem.style.left;
            node.style.top = elem.style.top;
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

        let a = Math.floor(node[src_prop] * scale) + ofs;
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
    on_show_poselib() {
      // this.is_show_poselib = false;
    },
    async init_ui() {
      let config = await api.get("/config.json");
      this.config = config;
      this.bone_map = config.map.concat(config.poselib);

      // this.$store['config'] = config
      this.poselib = config.poselib;
      console.log(api, config);
    }
  }
};
