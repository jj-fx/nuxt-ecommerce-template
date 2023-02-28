<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content">
      <!-- Any other Bulma elements you want -->
      <div v-model="props.file.name"></div>
      <div>{{ props.grounded }}</div>
      <ul>
        <li v-for="(item, index) in props.animals">{{ item }}</li>
      </ul>
      <div>{{ props.description }}</div>
      <div>{{ price }} PLN</div>
    </div>
    <button class="modal-close is-large" aria-label="close"></button>
  </div>
</template>

<script setup>
const props = defineProps({
  file: File,
  grounded: Boolean,
  animals: [String],
  description: String,
  price: Number
})
</script>

