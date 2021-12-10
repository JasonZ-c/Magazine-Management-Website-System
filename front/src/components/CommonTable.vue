<template>
  <div>
    <el-table :data="tableData" style="width: 100%" v-loading="config.loading">
    
      <el-table-column
        v-for="item in tableLabelList.filter(el => el.prop === 'image')"
        :key="item.prop"
        show-overflow-tooltip
        :label="item.label"
        :width="item.width ? item.width : 75"
      >
        <template slot-scope="scope">
          <span style="margin-left: 10px">
            <img
              :src="scope.row.imageUrl"
              alt=""
              style="width:100px;height:100px"
            />
          </span>
        </template>
      </el-table-column>
	  <!-- 这里对常规文本类型进行处理，对过滤出image和switch之后的字段进行循环绑定 -->
	  <el-table-column
        v-for="item in tableLabelList.filter(
          ele => ele.prop !== 'image' && ele.prop !== 'status'
        )"
        :key="item.prop"
        :label="item.label"
        :width="item.width ? item.width : 180"
      >
        <template slot-scope="scope">
          <span style="margin-left:10px">{{ scope.row[item.prop] }}</span>
        </template>
      </el-table-column>
	
	<!-- 处理switch开关 -->
	<el-table-column
        v-for="item in tableLabelList.filter(ele => ele.prop === 'status')"
        :key="item.prop"
        :label="item.label"
        :width="item.width ? item.width : 50"
      >
        <template slot-scope="scope">
            <!-- switch开关：之所以disableed，是不希望在这里进行状态修改，而是通过编辑的方式提交post请求修改 -->
            <el-switch disabled v-model="scope.row.status"></el-switch>
        </template>
      </el-table-column>	
    </el-table>
	
	<!--数据操作列，可以根据实际情况进行逻辑处理 -->
	<el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)"
            >编辑</el-button
          >
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
            >删除</el-button
          >
        </template>
      </el-table-column>
  </div>
</template>

<script>
    export default {
  		// 接收父组件传参
        props: {
        	tableData: Array, // 存放父组件传递过来的表数据
        	tableLabelList: Array, // 存放父组件传递过来的表字段数据
        	config:Object	// 配置项，比如表格每一页多少条数据，数据的加载状态,v-loading指令
        },
        methods: {
            handleEdit(index, row) {
                console.log(index, row);
            },
            handleDelete(index, row) {
                console.log(index, row);
           }
    }
    }
</script>
<style lang="scss" scoped>
</style>
