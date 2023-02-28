<template>
  <div class="panel m-6">
    <p class="panel-heading">Add Housing</p>
    <div class="panel-block">
      <div class="file has-name is-fullwidth">
        <label class="file-label">
          <input @change="handleFile" class="file-input" type="file" name="resume">
          <span class="file-cta">
            <span class="file-icon">
              <i class="fas fa-upload"></i>
            </span>
            <span class="file-label">
              Choose a file…
            </span>
          </span>
          <span class="file-name">
            {{ fileName }}
          </span>
        </label>
      </div>
    </div>
    <div class="panel-block">
      <label class="checkbox">
        <input v-model="type" type="checkbox">
        Grounded
      </label>
    </div>
    <div class="panel-block">
      <div>
        <div class="m-1">Suitable for animals (multiselect):</div>
        <div class="select is-multiple is-fullwidth">
          <select v-model="animals" multiple size="8">
            <option value="cats">Cats</option>
            <option value="dogs">Dogs</option>
            <option value="birds">Birds</option>
            <option value="elephants">Elephants</option>
          </select>
        </div>
      </div>
    </div>
    <div class="panel-block">
      <textarea v-model="description" class="textarea" placeholder="Add detailed housing description here..."></textarea>
    </div>
    <div class="panel-block">
      <div>Price (PLN)</div>
      <input v-model="price" class="input" type="number">
    </div>
    <div class="panel-block">
      <p class="control">
        <button @click="preview" class="button is-success">
          Preview
        </button>
      </p>
    </div>
  </div>
  <AdminPreview
      v-if="showPreview"
      :file="file"
      :grounded="type"
      :animals="animals"
      :description="description"
      :price="price"
      @closePreview="closePreview"/>
</template>

<script setup>
const file = ref(undefined);
const fileName = ref('no file selected...');
const type = ref(false);
const animals = ref([]);
const description = ref('');
const price = ref(0);
const showPreview = ref(false);

const handleFile = (event) => {
  if (!!event.target.files[0]) {
    file.value = event.target.files[0];
    fileName.value = file.value.name;
  }
}

const preview = () => {
  showPreview.value = true;
}

const closePreview = () => {
  showPreview.value = false;
}
</script>
