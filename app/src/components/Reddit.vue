<template>
  <ion-app>
    <ion-header>
      <ion-navbar>
        <ion-title>
        </ion-title>
      </ion-navbar>
    </ion-header>
    <ion-content>
      <ion-list>
        <ion-item v-for="post in posts" v-bind:key="post.data.id">
          {{post.data.title}}
        </ion-item>
      </ion-list>
    </ion-content>
  </ion-app>
</template>

<script>
import SnowVueService from '../services/snow-data';

export default {
  name: 'Reddit',
  data () {
    return {
      posts: []
    }
  },
  created () {
    SnowVueService.getPosts().then(response => {
      this.posts = response.body.data.children;
    });
  }
};
</script>
