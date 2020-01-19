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
        <div id="map_container" :style="zoom_style">
          <div  v-for="(node, i) in item.node" :key="i"
          style="position:absolute"
          >
            <el-radio
              draggable="true"
              :id="node.bone_name"
              v-model="bone"
              :label="node.bone_name"
              :style="node.style"
              @change="on_sel_node(node)"
              >{{ node.bone_name }}
              {{ node.style.left + node.style.top }}</el-radio
            >
          </div>
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
<script src="./char_selector.js"></script>
