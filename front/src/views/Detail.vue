<template>
  <div class="dt">
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
      <el-col :span="24">  
        <el-card shadow="always" style="height:400px;width: 60%; margin-left: 20%; margin-top: 20px">
          <template #header>
              <div class="clearfix">
                  <span style="font-size:25px;margin-top: 0px; float: left">任务信息</span>
                  <el-form :inline="true" class="demo-form-inline">
                    <input type="file" name="imageFile" id="imageFile" style="margin-top: 6px">
                    <el-button type="primary" style="margin-top: 0px;float: right" @click="chimage" :disabled='!stated'>确认修改</el-button>
                  </el-form>  
              </div>
          </template>
          <div>
            <div class="picture">
              <img :src='sc' width="285" height="285" />
            </div>
            <div class="info">
              <el-form ref="form" :model="form" label-width="80px" id="selectForm">
                <el-form-item label="文章标题">
                  <el-input v-model="form.title" :disabled="true"></el-input>
                </el-form-item>
                <el-form-item label="文章作者">
                  <el-input v-model="form.author" :disabled="true"></el-input>
                </el-form-item>
                
                <el-form-item label="文章描述">
                  <el-input
                    type="textarea"
                    :rows="6"
                    v-model="form.desc"
                    :disabled="revised">
                  </el-input>
                </el-form-item>
              </el-form>
            </div>
          </div>
        </el-card>
      </el-col>  
    </el-row>
    
    
    <el-row>
      <el-col :span="24">
        <el-card shadow="always" style="width: 60%; margin-left:20%; margin-top: 20px;">
          <template #header>
              <div class="clearfix">
                  <span style="font-size:25px;margin-top: 0px;float: left">附件下载</span>
                <!--<el-upload
				          class="upload-demo"
				          :auto-upload="false"
				          multiple
                          :limit="1"
				          :on-exceed="handleExceed"
                          :on-change="getFile"
				          :file-list="fileList"
                  style="margin-top: 0px;float: right">
                    <el-button type="primary" :disabled='!stated'>立即上传</el-button>
                  </el-upload>-->
                <!--accept中剩下需要添加的.doc, .docx, .xls, .xlsx"-->

                <el-upload
                  class="upload-demo"
                  ref="upload"
                  accept=".pdf" 
                  action="https://jsonplaceholder.typicode.com/posts/"
                  multiple=""
                  :limit="1"
                  :on-exceed="handleExceed"
                  :on-change="getTempFile"
                  :file-list="fileList"
                  :auto-upload="false">
                  <el-button slot="trigger" size="middle" type="primary">选取文件</el-button>
                  <el-button style="margin-left: 10px;" size="middle" type="success" @click="getFile">上传到该文章</el-button>
                  <div slot="tip" class="el-upload__tip">只能上传PDF文件</div>
                </el-upload>
                  
              </div>
          </template>
          <el-link :href="attachment" target="_blank" :underline='false' :disabled="!stated">{{attachment_name}}</el-link>
        </el-card>
      </el-col>
    </el-row>
    
    <el-row>
      <el-col :span="24">
        <el-card shadow="always" style="width: 60%; margin-left:20%; margin-top: 20px; margin-bottom: 20px">
          <template #header>
              <div class="clearfix">
                  <span style="font-size:25px;margin-top: 0px;float: left">评论区</span>
                  <el-button type="primary" style="margin-top: 0px;float: right" @click="dialogFormVisible = true" :disabled='!stated'>添加评论</el-button>
                  <el-dialog title="评论" :visible.sync="dialogFormVisible">
                    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                      <el-form-item label="内容" prop="desc">
                        <el-input type="textarea" v-model="ruleForm.desc"></el-input>
                      </el-form-item>
                      <el-form-item>
                        <el-button type="primary" @click="submitForm('ruleForm')">创建</el-button>
                        <el-button @click="resetForm('ruleForm')">重置</el-button>
                      </el-form-item>
                    </el-form>
                  </el-dialog>
              </div>
          </template>
          <el-table
            :data="tableData"
            style="width: 100%">
            <el-table-column
              prop="date"
              label="日期"
              width="210">
            </el-table-column>
            <el-table-column
              prop="name"
              label="用户名"
              width="210">
            </el-table-column>
            <el-table-column
              prop="address"
              label="评论内容">
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>
    </el-row>
    
    <el-row>
      <div class='queren'>
        <el-button type="success" @click="pass()" :disabled='whether_staff'>通过PASS</el-button>
      </div>
    </el-row>
    
  </div>
  
</template>

<script>
import axios from 'axios';
axios.defaults.baseURL = '/api';

export default {
  inject:['reload'],
  data() {
    return {
      sc: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
      attachment: ' ',
      attachment_name: '',
      fileList: [],
      tempFile:'',
      revised: '',
      whether_staff: true,
      dialogFormVisible: false,
      form:{
        title: '',
        author: '',
        desc: ''
      },
      dept: '',
      stated: '',
      my_id: '',
      tableData: [],
      ruleForm: {
          desc: ''
      },
      rules: {
          desc: [
            { required: true, message: '评论不能为空', trigger: 'blur' }
          ]
      }      
    };
  },
  mounted() {
    this.showdetail();
  },
  methods: {
    showdetail() {
      let that = this; 
      that.fileList = [];
      that.dept = that.$route.params.name;
      that.stated = that.$store.state.isLoggedIn;
      that.my_id = that.$route.params.id;
      const path = '/task_detail';
      const formData = new FormData();
	  formData.append('dept',that.dept);
      formData.append('mid',that.my_id);
      formData.append('sta',that.stated);
      if (that.$store.state.user==null){
        formData.append('uname',"fuck!");
      }
      else{
        formData.append('uname',that.$store.state.user.username);
      }
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      };
      axios.post(path,formData,config).then(function (response) {
        that.form.title = response.data.title;
        that.form.author = response.data.created_by;
        that.form.desc = response.data.describe;
        that.tableData = response.data.comments;
        that.sc = response.data.imagesrc;
        if(that.stated == true){
          if(response.data.has_att == 'yes'){
            that.attachment = response.data.attachment;
            that.attachment_name = response.data.attachment_name;
          }
          else{
            that.attachment_name = '暂时没有附件添加';
          }
          if(that.form.author == that.$store.state.user.username){
            that.revised = false;
          }
          else that.revised = true;
          if(response.data.is_prof == 'yes'){
            that.whether_staff = false;
          }
          else that.whether_staff = true;
        }
        else{
          that.attachment = '';
          that.attachment_name = '请先登录查看附件';
          that.revised = true;
        }
      }).catch(function (error) {
        alert(error);
      })
    },
    chimage() {
	  let that = this;
      let f = document.getElementById("imageFile").files[0];
	  const path = '/task_detail_feng';
	  const formData = new FormData();
	  formData.append('picfile',f);
      formData.append('mid',that.$route.params.id);
      formData.append('content',that.form.desc);
	  let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      };
	  axios.post(path,formData,config).then(function (response) {
        if(response.data.information == 'isjpg' && that.stated == true){
          that.sc = response.data.imgsrc;
          //that.$router.go(0);
          alert('成功修改任务信息');
        }
        else if(response.data.information == 'notjpg' && that.stated == true){
          alert('请使用.jpg图片作为头像');
        }
        else alert('请先登录哦');
      }).catch(function (error) {
        alert(error);
      })
    },
    submitForm(formName) {
      let that = this;
      that.$refs[formName].validate((valid) => {
        if (valid) {
          const path = '/task_addcomment';
	      const formData = new FormData();
	      formData.append('people',that.$store.state.user.username);
          formData.append('mid',that.$route.params.id);
          formData.append('content',that.ruleForm.desc);
	      let config = {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          };
	      axios.post(path,formData,config).then(function (response) {
            that.dialogFormVisible = false;
            that.reload();
            alert(response.data.mess);
          }).catch(function (error) {
            that.dialogFormVisible = false;
            alert(error);
          })
          //alert('submit!');
        }
        else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm(formName) {
        this.$refs[formName].resetFields();
    },
    handleExceed(files) {
	    this.fileList = [];
        this.$message.error(`当前限制选择 1 个文件，本次选择了 ${files.length} 个文件`);
    },
    getTempFile(file,fileList){
      //分别为pdf
      ///docx/doc文件未添加？如何添加 || 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' || 'application/msword'
      var isValid = false;
      if (file.raw.type == 'application/pdf'){
        isValid=true
      };
      //alert(isValid);
      if (!isValid){
        this.fileList = [];
        this.$message.error(`当前只支持pdf文件`);
      }
      else{
        this.tempFile=file
        this.fileList=fileList
        //console.log(isValid)
        //console.log(file.raw.type)
        //alert(isValid)
      }
    },
    getFile(){
      let that = this;
      //this.fileList = [];
      console.log(that.tempFile);
      console.log(that.fileList);
      //alert(file)//undefined error?
      //let that = this;
      const path = '/task_addfile';
	  const formData = new FormData();
	  formData.append('people',that.$store.state.user.username);
      formData.append('mid',that.$route.params.id);
      formData.append('content',that.tempFile.raw);//q:未收到file
	  let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      };
	  axios.post(path,formData,config).then(function (response) {
        that.attachment = response.data.attachment;
        that.attachment_name = response.data.attachment_name;
        //that.reload();
        alert(response.data.mess);
      }).catch(function (error) {
        alert(error);
      })
    },
    pass(){
      let that = this;
      const path = '/task_pass';
	  const formData = new FormData();
      formData.append('mid',that.$route.params.id);
	  let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      };
	  axios.post(path,formData,config).then(function (response) {
        alert(response.data.mess);
      }).catch(function (error) {
        alert(error);
      })
    },
  }
};

</script>

<style scoped>
.dt {
  margin-top: 1px;
}
.el-tag {
  font-size: 16px;
  width: 100%;
}
.info {
  height: 100%;
  width:72%;
  float:right;
}
.picture {
  width:25%;
  float:left;
}
#selectForm >>> .el-form-item__label {
  font-size: 16px;
}
.el-link {
  font-size: 18px;
}
.queren{
  margin-bottom: 40px;
}
</style>
