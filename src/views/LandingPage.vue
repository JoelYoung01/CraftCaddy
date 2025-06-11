<script setup lang="ts">
import BugZapLogoTransparent from "@/assets/bugzapper-transparent.png";
import FadeIn from "@/components/FadeIn.vue";
</script>

<template>
  <v-container max-width="500">
    <section id="title">
      <div class="mx-auto">
        <v-img :src="BugZapLogoTransparent" width="200" aspect-ratio="1" />
      </div>
      <h1 class="text-center text-h2 font-weight-bold mb-8">Bug Zapper</h1>
      <div>
        <v-btn
          to="/bug/report/"
          color="primary"
          variant="outlined"
          class="w-100 mb-5"
          rounded
          size="large"
        >
          Report a Bug
        </v-btn>
        <v-btn
          to="/feature/request/"
          color="primary"
          variant="outlined"
          rounded
          size="large"
          class="w-100 mb-5"
        >
          Request a Feature
        </v-btn>
      </div>
    </section>

    <section id="about">
      <h2 class="text-h4 font-weight-bold mb-5">What is Bug Zapper?</h2>
      <FadeIn class="mb-10">
        <h3 class="text-color-primary">Catch bugs early</h3>
        <p>
          Bug Zapper provides a clean and simple interface for your users to report bugs in detail,
          including screenshots and system information.
        </p>
      </FadeIn>
      <FadeIn class="mb-10">
        <h3 class="text-color-primary">Track user feedback</h3>
        <p>
          Bug Zapper allows users to view and comment on bugs to promote user feedback and track
          your users' interest and priority.
        </p>
      </FadeIn>
      <FadeIn class="mb-10">
        <h3 class="text-color-primary">Monitor bug status</h3>
        <p>
          Bug Zapper provides a comprehensive dashboard for app owners to track bug status, view
          summary statistics, and understand the overall health of their applications at a glance.
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
