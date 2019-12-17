import Vue from 'vue';
import Router from 'vue-router';
import Resort from '@/components/Resort';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Resort',
      component: Resort
    }
  ]
});
