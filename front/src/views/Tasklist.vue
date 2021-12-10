<template>
  <div class="tklist">
    <el-row>
      <el-col :span="24">
        <div class='biaoqian' v-if="stated == false">
          <el-tag type="danger" size='medium'>您还未登录该系统，不能查看附件</el-tag>
        </div>
        <div class='biaoqian' v-else>
          <el-tag type="success" size='medium'>您已经成功登录系统</el-tag>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <span style="font-size:50px;margin-top: 10px;">{{dept}}学院</span>
    </el-row>
    <el-row>
      <el-col :span="2">
        <el-divider direction="vertical"></el-divider>
        <el-button type="primary" size="small" @click="showlist(1)">正式文章</el-button>
      </el-col>
      <el-col :span="2">
        <el-divider direction="vertical"></el-divider>
        <el-button type="primary" size="small" @click="showlist(0)">待审文章</el-button>
      </el-col>
    </el-row>
    
    <el-row>
      <el-col :span="24">
        <el-table
          :data="tableData"
          style="width: 100%; margin-top: 20px">
          <el-table-column type="index" width="150" label="序号" align="center"></el-table-column>
          
          <el-table-column prop="imagesrc" label="文章封面" width="100" align="center">
              <template slot-scope="scope">            
                 <img :src="scope.row.imagesrc" width="80" height="80" />
              </template>         
          </el-table-column>
          
          <el-table-column prop="title" label="文章标题" width="210" align="center"></el-table-column>
          
          <el-table-column prop="bian" label="文章编号" width="150" align="center"></el-table-column>

          <el-table-column
            label="创建日期"
            width="210" align="center">
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <span style="margin-left: 10px">{{ scope.row.date }}</span>
            </template>
          </el-table-column>
          
          <el-table-column prop="created_by" label="创建者" width="210" align="center"></el-table-column>
          
          <el-table-column prop="send_to" label="发送给" width="210" align="center"></el-table-column>
          
          
          
          
          <el-table-column
            label="完成状态"
            width="210" align="center">
            <template slot-scope="scope">
              <el-tag size="medium">{{ scope.row.comp }}</el-tag>
            </template>
          </el-table-column>
          
          <el-table-column label="操作" align="center">
            <template slot-scope="scope">
              <el-button
                size="medium"
                @click="handleEdit(scope.$index, scope.row)">查看详情</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
    
    
    
  </div>
</template>

<script>
import axios from 'axios';
axios.defaults.baseURL = '/api';

export default {
  name: 'Tasklist',
  data() {
    return {
      name: 'lis',
      dept: 'no',
      stated: 'no',
      
      /*tableData: [{
          date: '2016-05-02',
          imagesrc: 'http://demo26.crmeb.net/uploads/attach/2020/04/27/b2bf3cf3be8a983c1920da54fb9f8579.jpg',
          title: 'test1',
          created_by: 'stu1',
          send_to: 'stu12',
          comp: '已完成'
        }, {
          date: '2016-05-04',
          imagesrc: 'http://demo26.crmeb.net/uploads/attach/2020/04/27/b2bf3cf3be8a983c1920da54fb9f8579.jpg',
          title: 'test1',
          created_by: 'stu1',
          send_to: 'stu12',
          comp: '已完成'
        }, {
          date: '2016-05-01',
          imagesrc: 'http://demo26.crmeb.net/uploads/attach/2020/04/27/b2bf3cf3be8a983c1920da54fb9f8579.jpg',
          title: 'test1',
          created_by: 'stu1',
          send_to: 'stu12',
          comp: '已完成'
        }, {
          date: '2016-05-03',
          imagesrc: 'http://demo26.crmeb.net/uploads/attach/2020/04/27/b2bf3cf3be8a983c1920da54fb9f8579.jpg',
          title: 'test1',
          created_by: 'stu1',
          send_to: 'stu12',
          comp: '已完成'
      }],*/
      tableData: []
      
    };
  },
  mounted() {
    this.showlist(1);
  },
  methods: {
    showlist(is_comp){
      let that = this; 
      that.dept = that.$route.params.name;
      that.stated = that.$store.state.isLoggedIn;
      const path = '/task_list';
      const formData = new FormData();
	  formData.append('type',that.dept);
      if(is_comp == 1)
          formData.append('co','yes');
      else
          formData.append('co','no');
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      };
      axios.post(path,formData,config).then(function (response) {
        that.tableData = response.data.main;
      }).catch(function (error) {
        alert(error);
      })
    },
    handleEdit(index, row){
      let that = this;
      //console.log(index, row);
      this.$router.push({
        path: '/tasklist/'+that.dept+'/'+row.bian});
    },
  }
  
  
  
  
  
};
</script>

<style scoped>
.tklist {
  margin-top: 1px;
}
.el-tag {
  font-size: 16px;
  width: 100%;
}
.el-button {
  font-size: 16px;
}
</style>
