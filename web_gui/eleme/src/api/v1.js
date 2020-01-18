import axios from "axios";

export const api = {
  hwnd: null,
  bpy_filename: null,
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
  async run_bpy(hwnd, bpy_filename) {
    if (hwnd) {
      let res = await axios.post(`/exec`, { hwnd: hwnd, bpy: bpy_filename });
      console.log(res);
      return new Promise(resolve => {
        resolve(res);
      });
    } else {
      console.log("no hwnd");
    }
  }
};
