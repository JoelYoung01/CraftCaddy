<script setup lang="ts">
import FadeIn from "@/components/FadeIn.vue";
import Logo from "@/assets/app_logo.png";
</script>

<template>
  <v-container max-width="1000">
    <section id="title">
      <v-row>
        <v-col cols="12" lg="4">
          <v-img :src="Logo" />
        </v-col>
        <v-col cols="12" lg="8">
          <h1 class="text-h1">Idea</h1>
          <h1 class="text-h1">Plan</h1>
          <h1 class="text-h1">DO</h1>
        </v-col>
      </v-row>
    </section>

    <section id="about">
      <h2 class="text-h4 font-weight-bold mb-5">How it works</h2>
      <FadeIn class="mb-10">
        <h3 class="text-color-primary">Start with an Idea</h3>
        <p>
          You are enjoying your morning coffee on the deck and suddenly, an idea hits you for some
          sort of project. Maybe it's a new app, or a different way of designing that shelf you've
          been thinking about. Quick! Add it to your CraftCaddy!
        </p>
      </FadeIn>
      <FadeIn class="mb-10">
        <h3 class="text-color-primary">Plan your project</h3>
        <p>
          As the idea continues to grow, you begin thinking through the details. You consider the
          materials and expenses you'll need, and record them in CraftCaddy. You begin to form a
          process of steps, which you record as tasks within CraftCaddy.
        </p>
      </FadeIn>
      <FadeIn class="mb-10">
        <h3 class="text-color-primary">Do it!</h3>
        <p>
          Let the fun begin! You can use CraftCaddy to track your progress, and to record the
          materials and expenses you came across as you worked on your app. When you're done, snap
          some pics so you can showcase your project on your profile and share it with your friends!
        </p>
      </FadeIn>
    </section>

    <section id="register">
      <h2 class="text-h4 font-weight-bold mb-5">Register Your App</h2>
      <FadeIn>
        <v-row>
          <v-col cols="12" lg="4">
            <v-card class="h-100">
              <div class="text-h6 px-2 py-3 text-center text-primary">1 App</div>
              <v-card-subtitle class="text-center">Free</v-card-subtitle>
              <v-card-text class="text-center">
                Perfect for small projects or personal use.
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12" lg="4">
            <v-card class="h-100">
              <div class="text-h6 px-2 py-3 text-center text-primary">Up to 5 Apps</div>
              <v-card-subtitle class="text-center">$5/mo</v-card-subtitle>
              <v-card-text class="text-center">
                Ideal for small teams and growing projects.
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12" lg="4">
            <v-card class="h-100">
              <div class="text-h6 px-2 py-3 text-center text-primary">More than 5 Apps</div>
              <v-card-subtitle class="text-center">$1/mo per app</v-card-subtitle>
              <v-card-text class="text-center">
                Best for larger teams and enterprises.
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <div class="mt-4">
          <v-btn color="primary" block size="large" to="/get-started">Get Started!</v-btn>
        </div>
      </FadeIn>
    </section>
  </v-container>
</template>

<style scoped>
section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-bottom: 4rem;
  min-height: 100vh;
  gap: 1rem;
}

#title {
  min-height: calc(100vh - 5rem);
}
</style>
