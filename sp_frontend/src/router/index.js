import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Campaigns from '@/components/show_campaigns'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
	{
      path: '/Campaigns',
      name: 'Campaigns',
	  component: Campaigns
      
    }
  ]
})
