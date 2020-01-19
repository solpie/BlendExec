import axios from "axios";
const sel_bone = (rig, bone_name) => {
    return `
import bpy
def select_bone(rig, bone):
    #rig = 'rig'
    #bone = 'c_hand_fk.r'
    mode = bpy.context.mode
    if mode == 'OBJECT':
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[rig].select_set(1)
        bpy.ops.object.posemode_toggle(1)
    bpy.ops.pose.select_all(action='DESELECT')
    armt = bpy.data.armatures[bpy.data.objects[rig].data.name]
    armt.bones[bone].select = True
    pass
select_bone('${rig}', '${bone_name}')
    `;
};
export const api = {
  hwnd: null,
  bpy_filename: null,
  bpy_sel_bone: sel_bone,
  async get(url) {
    console.log("api get", url);
    let res = await axios.get(url);
    return new Promise((resolve, reject) => {
      if (res.status === 200) {
        resolve(res.data);
      } else {
        reject(res);
      }
    });
  },
  async post(url) {
    console.log("api get", url);
    let res = await axios.get(url);
    return new Promise((resolve, reject) => {
      if (res.status === 200) {
        resolve(res.data);
      } else {
        reject(res);
      }
    });
  },
  async get_hwnd() {
    let res = await api.get("/hwnd");
    return new Promise(resolve => {
      resolve(res);
    });
  },
  async get_bpy() {
    let res = await api.get("/bpy");
    console.log(res);
    return new Promise(resolve => {
      resolve(res);
    });
  },
  async save_bone_map(config) {
    let res = await axios.post(`/save`, {
      filename: "config.json",
      data: JSON.stringify(config)
    });
    console.log(res);
    return new Promise(resolve => {
      resolve(res);
    });
  },
  async run_bpy_str(str) {
    let hwnd = api.hwnd;
    if (hwnd) {
      let res = await axios.post(`/exec`, { hwnd: hwnd, str: str });
      console.log(res);
      return new Promise(resolve => {
        resolve(res);
      });
    } else {
      console.log("no hwnd");
    }
  },
  async run_bpy(hwnd, bpy_filename) {
    if (hwnd) {
      let res = await axios.post(`/exec`, { hwnd: hwnd, bpy: bpy_filename ,str:''});
      console.log(res);
      return new Promise(resolve => {
        resolve(res);
      });
    } else {
      console.log("no hwnd");
    }
  }
};
