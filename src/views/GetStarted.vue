<script setup lang="ts">
const selectedPlan = ref("free");
const currentStep = ref(1);

const selectPlan = (plan: string) => {
  selectedPlan.value = plan;
};
</script>

<template>
  <v-container>
    <h1 class="mb-5">Get Started with <span class="text-primary">BugZapper</span></h1>

    <v-window v-model="currentStep">
      <v-window-item :value="1">
        <v-card
          class="py-3 px-5 mb-3"
          :class="{
            'border-primary': selectedPlan === 'free',
            'border-unselected': selectedPlan !== 'free'
          }"
          @click="selectPlan('free')"
        >
          <div class="d-flex justify-space-between">
            <div class="text-h6 text-primary">Hobby</div>
            <v-icon v-if="selectedPlan === 'free'" icon="mdi-check" color="primary" />
          </div>
          <div class="text-medium-emphasis">Free</div>
          <div class="">+ One App</div>
        </v-card>

        <v-card
          class="py-3 px-5 mb-3"
          :class="{
            'border-primary': selectedPlan === 'pro',
            'border-unselected': selectedPlan !== 'pro'
          }"
          @click="selectPlan('pro')"
        >
          <div class="d-flex justify-space-between">
            <div class="text-h6 text-primary">Pro</div>
            <v-icon v-if="selectedPlan === 'pro'" icon="mdi-check" color="primary" />
          </div>
          <div class="text-medium-emphasis">$5/month</div>
          <div class="">+ Up to 5 Apps</div>
        </v-card>

        <v-card
          class="py-3 px-5 mb-3"
          :class="{
            'border-primary': selectedPlan === 'enterprise',
            'border-unselected': selectedPlan !== 'enterprise'
          }"
          @click="selectPlan('enterprise')"
        >
          <div class="d-flex justify-space-between">
            <div class="text-h6 text-primary">Enterprise</div>
            <v-icon v-if="selectedPlan === 'enterprise'" icon="mdi-check" color="primary" />
          </div>
          <div class="text-medium-emphasis">$10/month</div>
          <div class="">+ Up to 10 Apps</div>
        </v-card>

        <v-btn
          color="primary"
          :disabled="selectedPlan === 'free'"
          block
          size="large"
          @click="currentStep = 2"
          >Next</v-btn
        >
      </v-window-item>

      <v-window-item :value="2">
        <v-card class="py-3 px-5 mb-3">
          <p>
            <span class="text-primary">Unfortuantely</span>, I haven't set up payment processing
            yet. So you can't actually sign up for this tier. But you can sign up for the
            <span class="text-primary">Hobby</span> tier for free. Once I set up payment processing,
            you can updgrade to the <span class="text-primary">Pro</span> or
            <span class="text-primary">Enterprise</span> tier!
          </p>
        </v-card>

        <v-btn color="primary" block size="large" @click="currentStep = 1">Back</v-btn>
      </v-window-item>
    </v-window>
  </v-container>
</template>

<style scoped>
.border-primary {
  border: 2px solid rgba(var(--v-theme-primary), 0.5);
}

.border-unselected {
  border: 2px solid rgba(var(--v-theme-surface), 0.5);
}
</style>
