<script setup lang="ts">
import { useSessionStore } from "@/stores/session";

const sessionStore = useSessionStore();
</script>

<template>
  <div class="header-bar d-flex text-black font-weight-bold justify-space-between">
    <RouterLink v-if="sessionStore.isLoggedIn" to="/dashboard"> Dashboard </RouterLink>
    <RouterLink v-else to="/"> Home </RouterLink>
    <RouterLink v-if="!sessionStore.isLoggedIn" to="/login"> Log In </RouterLink>
    <RouterLink v-else to="/account"> My Account </RouterLink>
  </div>
</template>

<style scoped>
.header-bar {
  padding: 1rem;
  margin-bottom: 1rem;
}

a {
  color: rgba(var(--v-theme-on-surface), 0.8);
}

.router-link-active {
  color: rgb(var(--v-theme-primary));
}
</style>
