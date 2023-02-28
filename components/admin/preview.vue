<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content">
      <!-- Any other Bulma elements you want -->

      <div class="card">
        <div class="card-content">
          <div class="media">
            <figure class="media-left">
              <p class="image is-128x128">
                <img v-if="file" :src="sourceImage">
                <img v-else src="/img/no-image.png">
              </p>
            </figure>
            <div class="card-content" style="width: 100%">

              <div class="panel-block">
                <div v-if="grounded" class="tag is-success is-medium">Overground</div>
                <div v-else class="tag is-warning is-medium">Arboreal</div>
              </div>

              <div class="panel-block">
                <ul>
                  <li class="tag is-info m-1" v-for="(item, index) in animals">{{ item }}</li>
                </ul>
              </div>

              <div class="panel-block">
                <div>{{ description }}</div>
              </div>

              <div class="panel-block">
                <div>Price: <strong>{{ price }} PLN</strong></div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="card-content">
        <div>
          <button @click="$emit('closePreview')" class="button is-warning">Go Back...</button>
          <button class="button is-info is-pulled-right">I'm done! Save!</button>
        </div>
      </div>

    </div>
    <button @click="$emit('closePreview')" class="modal-close is-large" aria-label="close"></button>
  </div>
</template>

<script setup>
// const animals = ['cats', 'dogs']
const sourceImage = ref(undefined);

const props = defineProps({
  file: File,
  grounded: Boolean,
  animals: Array,
  description: String,
  price: Number
})

onMounted(() => {
  if (props.file) sourceImage.value = URL.createObjectURL(props.file)
})
</script>
