<template>

<div >
    <p>
    <a v-for="tab of tabs"
    v-if='currentForm !=tab.link' 
    href="" v-on:click.prevent="currentForm = tab.link">
    {{tab.name}}</a>  
    </p>
    <p>      
    <component v-bind:is="currentForm "  
    v-bind:http='request'
    v-bind:namePage = 'namePage'
    v-bind:welcomeText = 'welcomeText'
    v-on:succesLogin='succesLogin'
    v-on:clickButton='clickButton'>
    </component>
    </p>
</div>

</template>

<script>

import mainPage from "./main-page.vue";
import login from "./login-page.vue";
import showUsers from "./show-user-page.vue";
import registerPage from "./register-page.vue";

export default {
    data () {
        return {
            tabs:[
                {link:'app-main-page',name:' Главная страница '},
                {link:'app-register-page',name:' Регистрация '},
                {link:'app-login-page',name:" Вход "},
                {link:'app-show-users',name:" Показать пользователей "}
            ],
            currentForm:'app-main-page',
            namePage:'Some name',
            welcomeText: 'stranger',
        }
    },
    methods:{
            clickButton:function (page){
                this.currentForm = page;
            },
            succesLogin:function(user){
                this.welcomeText = user;
                this.currentForm='app-main-page'
            },
            request:function (self,methodRequest,next) {
                let url = 'http://127.0.0.1:5000/'; 
                url = self.$el.action
                var data = new URLSearchParams(new FormData(self.$el))
                data.append('method',methodRequest);
                fetch(url, {
                headers: {'Content-Type': "application/x-www-form-urlencoded"},
                method: 'POST',
                body: data,
                }).then(response => response.json())
                .then(json=>(self.response=json))
            },
    },
    components:{
        appMainPage:mainPage,
        appRegisterPage:registerPage,
        appLoginPage:login,
        appShowUsers:showUsers,
    },

}
</script>

