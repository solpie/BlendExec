<template>
  <div>
    <!-- <el-collapse v-model="activeNames">
      <el-collapse-item title="node editor" name="1">
        <el-row>
          <el-col :span="12">
            <el-input size="mini" v-model="rig_object_name" :maxlength="20">
              <template slot="prepend">rig object name</template>
            </el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-button size="mini" @click="on_save">Save</el-button>
          </el-col>
        </el-row>
      </el-collapse-item>
    </el-collapse> -->
    <el-tabs
      v-if="bone_map"
      tab-position="right"
      style="height: 600px;position:relative"
    >
      <el-tab-pane
        v-for="(item, n1) in bone_map"
        :key="n1"
        :label="item.tab"
        style="height:600px;border: 1px solid #222"
      >
        <div>
          <el-image
            v-if="item.bg"
            style="width: 100%;"
            :src="item.bg"
            fit="contain"
            disabled
            id="map_bg"
            @load="on_map_bg_loaded"
          />
          <div
            style="position:absolute;left:0px;top:0px;width:100%;height:100%;"
          >
            <div id="modal1" @click="on_create_node($event, item)"></div>
          </div>
          <el-card
            id="bone_editor"
            v-show="is_edit_bone"
            :style="bone_editor_style"
          >
            <el-row>
              bone name
              <el-input size="mini" v-model="bone"> </el-input>
            </el-row>
            <el-row>
              rig object name
              <el-input size="mini" v-model="item.rig_object_name"> </el-input>
            </el-row>
            <el-row>
              <el-button size="mini" @click="on_del_node">Del</el-button>
              <el-button size="mini" @click="on_edit_bone_name">ok</el-button>
              <el-button size="mini" @click="on_save">Save</el-button>
            </el-row>
          </el-card>
          <div style="position:absolute;left:0px;top:0px">
           
            <el-button
            size="mini"
              @click="on_mirror_bone(item)"
              >Mirror bone</el-button
            >
            edit mode
             <el-switch
              v-model="is_edit_mode"
              active-color="#13ce66"
              inactive-color="#ff4949"
            >
            </el-switch>
          </div>
          <div id="map_container" :style="zoom_style">
            <div
              v-for="(node, i) in item.node"
              :key="i"
              style="position:absolute"
            >
              <el-radio
                size="medium"
                draggable="true"
                :id="node.bone_name"
                v-model="bone"
                :label="node.bone_name"
                :style="node.style"
                @change="on_sel_node($event, node)"
              >
                <span v-show="is_edit_mode">
                  {{ node.bone_name }}
                  <span v-show="is_edit_bone">
                    ({{
                      node.style.left.replace("px", "") +
                        "," +
                        node.style.top.replace("px", "")
                    }})
                  </span>
                </span>
              </el-radio>
            </div>
          </div>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<style>
#modal1 {
  position: absolute;
  left: 0px;
  width: 1920px;
  /* z-index: 0; */
  /* pointer-events: none; */
  height: 1080px;
  background: #000;
  opacity: 0.0;
}
</style>
<script src="./char_selector.js"></script>
