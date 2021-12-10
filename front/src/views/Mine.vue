<template>
  <div class="my">
    <el-row>
      <span style="font-size:50px;margin-top: 10px;">我的文章</span>
    </el-row>
    <el-row>
      <el-col :span="2">
        <el-divider direction="vertical"></el-divider>
        <el-button type="primary" size="small" @click="dialog = true">新建task</el-button>
        <el-drawer
          title="新建task"
          :visible.sync="dialog"
          direction="rtl"
          custom-class="demo-drawer"
          ref="drawer"
          >
          <div class="demo-drawer__content">
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
              <el-form-item label="任务标题" prop="name">
                <el-input v-model="ruleForm.name"></el-input>
              </el-form-item>

              <el-form-item label="添加封面" prop="imageFile" >
                <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，若不上传则使用默认封面</div><!--没显示出来？？--> 
                <input placeholder="请输入内容" type="file" name="imageFile" id="imageFile" style="margin-top: 6px" > <!--</input>--> 
                
              </el-form-item>
                         

              <el-form-item label="选择分区" prop="type1">
                <el-checkbox-group v-model="ruleForm.type1" v-for="(profs,i) in list10" :key="i" :min="0" :max="1">
                  <el-checkbox :label="profs.label" name="type1"></el-checkbox>
                </el-checkbox-group>
              </el-form-item>

              <el-form-item label="任务描述" prop="desc">
                <el-input type="textarea" v-model="ruleForm.desc"></el-input>
              </el-form-item>

              <el-form-item label="提交附件" prop="file">
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
                  <div slot="tip" class="el-upload__tip">只能上传PDF文件</div>
                </el-upload>
              </el-form-item>
              
              <el-form-item>
                <el-button @click="cancelForm">取 消</el-button>
                <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-drawer>
        
        
        
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
          
          <el-table-column label="操作1" align="center" width="210">
            <template slot-scope="scope">
              <el-button
                size="medium"
                @click="handleEdit(scope.$index, scope.row)">查看详情</el-button>
            </template>
          </el-table-column>
          
          <el-table-column label="操作2" align="center">
            <template slot-scope="scope">
              <el-button
                size="medium"
                @click="handletest(scope.$index, scope.row)" :disabled='!is_admin'>发送给老师</el-button>
                
              <el-dialog title="发送文件" :visible.sync="dialogFormVisible">
                <el-form :model="ruleForm1" :rules="rules1" ref="ruleForm1" label-width="100px" class="demo-ruleForm">
                  <el-form-item label="发送对象" prop="type">
                    <el-checkbox-group v-model="ruleForm1.type" v-for="(profs,i) in list_prof" :key="i" :max='max'>
                      <el-checkbox :label="profs.label" name="type"></el-checkbox>
                    </el-checkbox-group>
                  </el-form-item>
                  <el-form-item>
                    <el-button @click="dialogFormVisible = false">取 消</el-button>
                    <el-button type="primary" @click="handleSendemail()">确 定</el-button>
                  </el-form-item>
                </el-form>
              </el-dialog>

                
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
  name: 'mine',
  inject:['reload'],
  data() {
    return {
      sc: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
      stated: 'no',
      max: 1,
      username: 'none',
      dept: 'mytask',
      is_admin: false,
      tempFile:'',
      hasFile: false,
      fileList:'',
      obj_test: '',
      /*tableData: [{
          date: '2016-05-02',
          imagesrc: 'http://demo26.crmeb.net/uploads/attach/2020/04/27/b2bf3cf3be8a983c1920da54fb9f8579.jpg',handleClose
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
      tableData: [],
      dialog: false,
      gridData: [
          {
            date: '2016-05-02',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
          }, {
            date: '2016-05-04',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
          }, {
            date: '2016-05-01',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
          }, {
            date: '2016-05-03',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
          }
      ],
      list: [
        {label: '学院管理员'},
      ],
      list10: [
        {label: '分区1'},
        {label: '分区2'},
        {label: '分区3'},
        {label: '分区4'},
      ],//分区
      list_prof: [
        {label: 'prof1'},
        {label: 'prof2'},
        {label: 'prof3'},
      ],
      ruleForm1: {
          type: [],
      },
      ruleForm: {
          name: '',
          //type: [],
          type1: [],
          //imageFile:
          desc: ''
      },
      formLabelWidth: '100px',
      timer: null,
      rules: {
          name: [
            { required: true, message: '请输入任务标题', trigger: 'blur' },
            //{ min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
          ],
          type: [
            { type: 'array', required: true, message: '请至少选择一个对象', trigger: 'change' }
          ],
          type1: [
            { type: 'array', required: true, message: '只能选择一个对象', trigger: 'change'}
            //{min=1,max=1}
          ],//分区
          desc: [
            { required: true, message: '请填写任务描述', trigger: 'blur' },
            
          ]
      },
      rules1: {
          type: [
            { type: 'array', required: true, message: '请至少选择一个对象', trigger: 'change' }
          ]
      }

    };
  },
  mounted() {
    this.myshowlist();
  },
  methods: {
    myshowlist(){
      let that = this; 
      that.stated = that.$store.state.isLoggedIn;
      that.username = that.$store.state.user.username;
      //console.log(that.$store.state.user.username);
      const path = '/task_mine';
      const formData = new FormData();
	  formData.append('uname',that.username);
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      };
      axios.post(path,formData,config).then(function (response) {
        that.tableData = response.data.main;
        that.list_prof = response.data.prof_name;
        that.sc = response.data.imagesrc;
        let ad = response.data.is_admin;
        if(ad == 'yes'){
          that.is_admin=true;
        }
        //console.log(that.is_admin);
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
        this.tempFile=file;
        this.fileList=fileList;
        this.hasFile=true;
        //console.log(isValid)
        //console.log(file.raw.type)
        //alert(isValid)
      }
    },
    submitForm(formName) {
      let that = this;
      let f1 = document.getElementById("imageFile").files[0];
      //const path1 = '/task_detail_feng';//picture fengmian
      if (that.hasFile){
        that.$refs[formName].validate((valid) => {
          if (valid) {
            //alert('submit!');
            const path = '/task_add';
            const formData = new FormData();
            formData.append('picfile',f1);//picture fengmian
	          formData.append('title',that.ruleForm.name);
            //formData.append('type',that.ruleForm.type);
            formData.append('type1',that.ruleForm.type1);
            formData.append('desc',that.ruleForm.desc);
            formData.append('uname',that.username);
            formData.append('content',that.tempFile.raw)
            let config = {
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            };
            axios.post(path,formData,config).then(function (response) {
              if(response.data.information == 'isjpg' && that.stated == true){
                that.sc = response.data.imgsrc;
                console.log(response.data.mess);
                that.dialog = false;
                that.reload();
                alert('成功新增任务');
                //that.$router.go(0);
                //alert('成功修改任务信息');
              }
              else if(response.data.information == 'notjpg' && that.stated == true){
                alert('请使用.jpg图片作为头像');
              }
              else alert('请先登录哦');
              /*console.log(response.data.mess);
              that.dialog = false;
              that.reload();
              alert('成功新增任务');*/
              //that.reload();
            }).catch(function (error) {
              alert(error);
            })
          } else {
            console.log('error submit!!');
            return false;
          }
        });
       }
       else{
        that.$message.error(`请上传附件`);
       }
    },
    cancelForm() {
      this.dialog = false;
    },
    handleSendemail(){
      let that = this;
      //console.log(that.obj_test);
      const path = '/task_sendmail';
      const formData = new FormData();
      formData.append('type',that.ruleForm1.type);
      formData.append('obj',that.obj_test.bian);
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      };
      axios.post(path,formData,config).then(function (response) {
        //console.log(response);
        that.dialogFormVisible = false;
        that.reload();
        alert(response.data.mess);
      }).catch(function (error) {
        //that.dialogFormVisible = false;
        that.dialogFormVisible = false;
        alert(error);
      })
    },
    handletest(index, row){
      let that = this;
      that.dialogFormVisible = true;
      that.obj_test = row;
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
