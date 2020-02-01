<template>
  <div>
    <div v-for="(item, i) in pose_arr" :key="i">
      <span>{{ item.name }}</span>
      <img :src="item.thumbnail" style="width:200px" />
    </div>
  </div>
</template>

<script>
export default {
  name: "Poselib",
  props: {
    pose_data: Object
  },
  data() {
    return {
      pose_arr: [{ name: "sitting", path: "pose.py", thumbnail: "" }]
    };
  },
  mounted() {
    this.$emit('show');
    this.get_poselib();
  },
  methods: {
    async get_poselib() {
      let poselib = this.pose_data;
      console.log("init poselib", poselib);
      for (let node of poselib.node) {
        let res = await this.$http.get(node.path);
        let thumbnail = res.data.match(/thumbnail="(.+)"/)[1];
        node.thumbnail = thumbnail;
      }
      this.pose_arr = poselib.node;
    }
  }
};
</script>
