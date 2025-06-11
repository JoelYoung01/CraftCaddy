<script setup lang="ts">
import { onMounted, ref, computed } from "vue";

const box = ref<HTMLElement | null>(null);
const hasFadedIn = ref(false);

const threshold = 0.1;

onMounted(() => {
  const handleScroll = () => {
    if (box.value && !hasFadedIn.value) {
      const rect = box.value.getBoundingClientRect();
      if (rect.top <= window.innerHeight * (1 - threshold)) {
        hasFadedIn.value = true;
        window.removeEventListener("scroll", handleScroll);
      }
    }
  };

  handleScroll(); // Initial check
  window.addEventListener("scroll", handleScroll);
});

const fadeInClass = computed(() => (hasFadedIn.value ? "fade-in-to" : "fade-in-from"));
</script>

<template>
  <div ref="box" :class="fadeInClass">
    <slot></slot>
  </div>
</template>

<style scoped>
.fade-in-from {
  opacity: 0;
  transform: translateY(20px);
}
.fade-in-to {
  transition:
    opacity 0.6s ease-out,
    transform 0.6s ease-out;
  opacity: 1;
  transform: translateY(0);
}
</style>
