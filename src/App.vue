<script setup lang="ts">
import { RouterView, useRoute } from "vue-router";
import NavbarHeader from "./components/NavbarHeader.vue";

const route = useRoute();

const mainClassList = computed(() => {
  let classes = "";

  if (route.meta.useShadedBackground) {
    classes += "shaded-bg";
  }

  return classes;
});
</script>

<template>
  <v-app>
    <v-main :class="mainClassList">
      <NavbarHeader />
      <RouterView />
    </v-main>
  </v-app>
</template>

<style scoped>
.shaded-bg {
  background-color: whitesmoke;
}
</style>
