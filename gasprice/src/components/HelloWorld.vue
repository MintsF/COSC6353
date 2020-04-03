<template>
  <div>
    <div class="main-container">
      <h2 >Profile</h2>
      <el-form :model="userlist" :rules="rules" ref="EditorUserForms" label-width="300px" class="demo-ruleForm" style="margin: 0px 330px">

        <el-form-item label="Full name" prop="full name" :label-width="formLabelWidth" >
         <el-col :span="21"> <el-input v-model="userlist.fullname" disabled></el-input></el-col>
        </el-form-item>

        <el-form-item label="Full Name" prop="username" :label-width="formLabelWidth">
         <el-col :span="21">
          <el-input v-model="userlist.username" ></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="Address1" prop="address1" :label-width="formLabelWidth">
         <el-col :span="21">  <el-input v-model="userlist.address1" placeholder="Please enter address required"></el-input></el-col>
        </el-form-item>

        <el-form-item label="Address2" prop="address2" :label-width="formLabelWidth">
         <el-col :span="21">  <el-input v-model="userlist.address2" placeholder="Please enter address optional"></el-input></el-col>
        </el-form-item>

        <el-form-item label="City" prop="city" :label-width="formLabelWidth">
         <el-col :span="21">  <el-input v-model="userlist.city" placeholder="Please enter city"></el-input></el-col>
        </el-form-item>

        <el-form-item label="State" prop="state" :label-width="formLabelWidth">
         <el-col :span="8">  
         <el-select v-model="userlist.state" placeholder="Please select one ">
           <el-option v-for="(item,index) in columeTypeArr" :key="index" :label="item.name" :value="item.abbreviation">
           </el-option>
         </el-select>

         </el-col>
        </el-form-item>
        <!-- <p> {{userlist}}</p> -->

        <el-form-item label="ZipCode" prop="zipcode" :label-width="formLabelWidth">
         <el-col :span="21">  <el-input v-model="userlist.zipcode" placeholder="Please enter Zipcode"></el-input></el-col>
        </el-form-item>

        <el-form-item label="Password" prop="password" :label-width="formLabelWidth">
          <el-col :span="8" style="text-align: left">
            <a @click="showdialog" style="text-align: left;color: blue">change password</a>
            <dialog-bar :show="show" :title="title" @hideModal="hideModal" @submit="changePassword">
              <div style="text-align: left">
                <el-form-item label="old password" prop="password" label-width="200px" >
                  <el-input placeholder="********" v-model="userlist.oldPassword" show-password   ></el-input>
                </el-form-item>

                <el-form-item label="new password" label-width="200px">
                  <el-input placeholder="********" v-model="userlist.newPassword" show-password   ></el-input>
                </el-form-item>

                <el-form-item label="confirm password" label-width="200px">
                  <el-input placeholder="********" v-model="userlist.confirmPassword" show-password   ></el-input>
                </el-form-item>
              </div>


            </dialog-bar>

          </el-col>
        </el-form-item>

        <el-form-item >
         <el-col :span="8" style="text-align: left"> 
          <el-button type="primary" @click="BacktoHome" style="text-align: left" >Back</el-button></el-col>
        <el-col :span="8" style="text-align: left">
          <el-button type="primary" @click="submit" style="text-align: right">Save</el-button></el-col>

        </el-form-item>

      </el-form>
    </div>

    <!-- EditorUserClick('userlist') -->
  </div>
  
</template>

<script >
  import dialogBar from './dialog.vue'

  export default{
       components:{
        'dialog-bar': dialogBar,
    },
    data(){
      return{
        title: 'Change password',
        show: false,
        
        userlist: { 
          userid: '',
          username: '',
          address1: '',
          address2: '',
          city: '',
          state: '',
          zipcode: '',
          oldPassword: '',
          newPassword: '',
          confirmPassword: '',
        },
        formLabelWidth: "150px",
        columeTypeArr:[
          {
              "name": "Alabama",
              "abbreviation": "AL"
          },
          {
              "name": "Alaska",
              "abbreviation": "AK"
          },
          {
              "name": "American Samoa",
              "abbreviation": "AS"
          },
          {
              "name": "Arizona",
              "abbreviation": "AZ"
          },
          {
              "name": "Arkansas",
              "abbreviation": "AR"
          },
          {
              "name": "California",
              "abbreviation": "CA"
          },
          {
              "name": "Colorado",
              "abbreviation": "CO"
          },
          {
              "name": "Connecticut",
              "abbreviation": "CT"
          },
          {
              "name": "Delaware",
              "abbreviation": "DE"
          },
          {
              "name": "District Of Columbia",
              "abbreviation": "DC"
          },
          {
              "name": "Federated States Of Micronesia",
              "abbreviation": "FM"
          },
          {
              "name": "Florida",
              "abbreviation": "FL"
          },
          {
              "name": "Georgia",
              "abbreviation": "GA"
          },
          {
              "name": "Guam",
              "abbreviation": "GU"
          },
          {
              "name": "Hawaii",
              "abbreviation": "HI"
          },
          {
              "name": "Idaho",
              "abbreviation": "ID"
          },
          {
              "name": "Illinois",
              "abbreviation": "IL"
          },
          {
              "name": "Indiana",
              "abbreviation": "IN"
          },
          {
              "name": "Iowa",
              "abbreviation": "IA"
          },
          {
              "name": "Kansas",
              "abbreviation": "KS"
          },
          {
              "name": "Kentucky",
              "abbreviation": "KY"
          },
          {
              "name": "Louisiana",
              "abbreviation": "LA"
          },
          {
              "name": "Maine",
              "abbreviation": "ME"
          },
          {
              "name": "Marshall Islands",
              "abbreviation": "MH"
          },
          {
              "name": "Maryland",
              "abbreviation": "MD"
          },
          {
              "name": "Massachusetts",
              "abbreviation": "MA"
          },
          {
              "name": "Michigan",
              "abbreviation": "MI"
          },
          {
              "name": "Minnesota",
              "abbreviation": "MN"
          },
          {
              "name": "Mississippi",
              "abbreviation": "MS"
          },
          {
              "name": "Missouri",
              "abbreviation": "MO"
          },
          {
              "name": "Montana",
              "abbreviation": "MT"
          },
          {
              "name": "Nebraska",
              "abbreviation": "NE"
          },
          {
              "name": "Nevada",
              "abbreviation": "NV"
          },
          {
              "name": "New Hampshire",
              "abbreviation": "NH"
          },
          {
              "name": "New Jersey",
              "abbreviation": "NJ"
          },
          {
              "name": "New Mexico",
              "abbreviation": "NM"
          },
          {
              "name": "New York",
              "abbreviation": "NY"
          },
          {
              "name": "North Carolina",
              "abbreviation": "NC"
          },
          {
              "name": "North Dakota",
              "abbreviation": "ND"
          },
          {
              "name": "Northern Mariana Islands",
              "abbreviation": "MP"
          },
          {
              "name": "Ohio",
              "abbreviation": "OH"
          },
          {
              "name": "Oklahoma",
              "abbreviation": "OK"
          },
          {
              "name": "Oregon",
              "abbreviation": "OR"
          },
          {
              "name": "Palau",
              "abbreviation": "PW"
          },
          {
              "name": "Pennsylvania",
              "abbreviation": "PA"
          },
          {
              "name": "Puerto Rico",
              "abbreviation": "PR"
          },
          {
              "name": "Rhode Island",
              "abbreviation": "RI"
          },
          {
              "name": "South Carolina",
              "abbreviation": "SC"
          },
          {
              "name": "South Dakota",
              "abbreviation": "SD"
          },
          {
              "name": "Tennessee",
              "abbreviation": "TN"
          },
          {
              "name": "Texas",
              "abbreviation": "TX"
          },
          {
              "name": "Utah",
              "abbreviation": "UT"
          },
          {
              "name": "Vermont",
              "abbreviation": "VT"
          },
          {
              "name": "Virgin Islands",
              "abbreviation": "VI"
          },
          {
              "name": "Virginia",
              "abbreviation": "VA"
          },
          {
              "name": "Washington",
              "abbreviation": "WA"
          },
          {
              "name": "West Virginia",
              "abbreviation": "WV"
          },
          {
              "name": "Wisconsin",
              "abbreviation": "WI"
          },
          {
              "name": "Wyoming",
              "abbreviation": "WY"
          }
        ],
        rules: {
        
          fullname: [{
            required: true,
            message: "please enter fullname"
          }],
          address1: [{
            required: true,
            message: "please enter address1"
          }],
          address2: [{
            required: false
          }],
          city: [{
            required: true,
            message: "please enter city"
          }],
          state: [{
            required: true,
            message: "please enter state"
          }],
          zipcode: [{
            required: true,
            message: "please enter zipcode"
          },
          {
            pattern: /(^\d{5}$)|(^\d{5}-\d{4}$)/,
            message: "number only"
          }],
          password: [{
            required: true,
            message: "please enter original password"
          }]
        }
      }
    },
    methods:{
        hideModal() {
            // 取消弹窗回调
            this.show = false
        },
        submit() {
            // 确认弹窗回调
            var userData =this.$qs.stringify ({
              userid: this.userlist.userid,
              username: this.userlist.username,
              address1: this.userlist.address1,
              address2: this.userlist.address2,
              city: this.userlist.city,
              state: this.userlist.state,
              zipcode: this.userlist.zipcode,
              oldPassword: this.userlist.oldPassword,
              newPassword: this.userlist.newPassword,
              confirmPassword: this.userlist.confirmPassword,
            });
            if(this.userlist.username && this.userlist.address1 && this.userlist.city && this.userlist.state && this.userlist.zipcode){
                this.$axios.post('/api/profile/',userData).then(res=>{
                    console.log(res)
                    }, function(){
                    console.log("Can not submit profile to server");
                    })
                this.$router.push('/FuelQuote')
            }
            this.show = false
        },
        showdialog(){
          this.show=true
        },
        BacktoHome(){
          this.$router.push('/FuelQuote')
        },
        changePassword(){
          if(this.userlist.newPassword && this.userlist.confirmPassword && this.userlist.confirmPassword == this.userlist.newPassword){
            this.show=false
          }
        },
    }
  }
  
</script>

<style type="text/css">

  .el-button--primary{
    font-family: "Roboto", sans-serif;
    font-weight: 600;
    background:linear-gradient(150deg,  #97c74e 0%, #2ab9a5 100%);
  }
</style>