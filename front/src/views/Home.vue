<template>
  <div class="home">
    <el-row>
      <el-col :span="6">
        <el-card :body-style="{ padding: '5px' }">
          <img src="http://127.0.0.1:8001/media/fengmian/default.jpg" class="image">
          <div style="padding: 14px;">
            <div class="pizi"> 
              <span>{{departments[0].name}}</span>
            </div>
            <div class="bottom clearfix">
              <el-button type="text" class="button" @click="chakan1">文章数目：{{departments[0].num}}</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
      
      <el-col :span="6">
        <el-card :body-style="{ padding: '5px' }">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
          <div style="padding: 14px;">
            <div class="pizi"> 
              <span>{{departments[1].name}}</span>
            </div>
            <div class="bottom clearfix">
              <el-button type="text" class="button" @click="chakan2">文章数目：{{departments[1].num}}</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card :body-style="{ padding: '5px' }">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
          <div style="padding: 14px;">
            <div class="pizi">
              <span>{{departments[2].name}}</span>
            </div>
            <div class="bottom clearfix">
              <el-button type="text" class="button" @click="chakan3">文章数目：{{departments[2].num}}</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card :body-style="{ padding: '5px' }">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
          <div style="padding: 14px;">
            <div class="pizi">
              <span>{{departments[3].name}}</span>
            </div>
            <div class="bottom clearfix">
              <el-button type="text" class="button" @click="chakan4">文章数目：{{departments[3].num}}</el-button>
            </div>
          </div>
        </el-card>
      </el-col>

    </el-row>
  </div>
</template>

<script>
import axios from 'axios';
axios.defaults.baseURL = '/api';

export default {
  name: "Home",
  //provide() {
    //eturn{
      //reload:this.getnum
    //}
  //},
  data() {
    return {
      departments: [
              { id: 1, name: "" ,num:0},
              { id: 2, name: "" ,num:0},
              { id: 3, name: "自动化学院" ,num:0},
              { id: 4, name: "经管学院" ,num:0}
      ],
    };
  },
  mounted() {
    this.getnum();
  },
  methods: {
    getnum() {
      var that = this;
      const path = '/list_count';
      axios.post(path).then(function (response) {
        that.departments[0].num = response.data.shulist[0];
        that.departments[1].num = response.data.shulist[1];
        that.departments[2].num = response.data.shulist[2];
        that.departments[3].num = response.data.shulist[3];
        that.departments[0].name = response.data.namelist[0];
        that.departments[1].name = response.data.namelist[1];
        that.departments[2].name = response.data.namelist[2];
        that.departments[3].name = response.data.namelist[3];
      }).catch(function (error) {
        alert(error);
      })
    },
    chakan1() {
      this.$router.push({
        //name: 'Tasklist',
        //params: {"dep": 'chemistry'}
        path: '/tasklist/chemistry'
      })
    },
    chakan2() {
      this.$router.push({
        //name: 'Tasklist',
        //params: {"dep": 'ee'}
        path: '/tasklist/cs'
      })
    },
    chakan3() {
      this.$router.push({
        //name: 'Tasklist',
        //params: {"dep": 'cs'}
        path: '/tasklist/ee'
      })
    },
    chakan4() {
      this.$router.push({
        //name: 'Tasklist',
        //params: {"dep": 'ee'}
        path: '/tasklist/physics'
      })
    },

  },  

};
</script>

<style scoped>
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    height: 300px;
    display: block;
    text-align: center;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  .clearfix:after {
      clear: both
  }
  .pizi {
    font-size: 20px;
    font-weight: bold;
  }
</style>
