<template>
  <v-container>
    <h2>Active Projects</h2>
    <v-row class="mb-3">
      <v-col cols="4">
        <v-card>
          <v-card-text> You have no active projects. </v-card-text>
          <v-card-actions>
            <v-btn>Create a new project</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <h2>Completed Projects</h2>
    <v-row>
      <v-col cols="4">
        <v-card>
          <v-card-text>You have no completed projects.</v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
