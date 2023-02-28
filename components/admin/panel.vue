<template>
  <div class="m-6">
    <nav class="panel">
      <p class="panel-heading">
        Pick a task...
      </p>
      <div class="panel-block">
        <p class="control has-icons-left">
          <input v-model="keyword" class="input" type="text" placeholder="Search">
          <span class="icon is-left">
        <i class="fas fa-search" aria-hidden="true"></i>
      </span>
        </p>
      </div>

      <a v-for="(item, index) in filtered" @click="pickTask" class="panel-block">
        <span class="panel-icon">
          <i class="fas fa-book" aria-hidden="true"></i>
        </span>
        {{ item }}
      </a>

      <div class="panel-block">
        <button @click="reset" class="button is-link is-outlined is-fullwidth">
          Reset all filters
        </button>
      </div>
    </nav>
  </div>
</template>

<script setup>
const router = useRouter();
const tasks = ref(['Add item', 'Edit item', 'Edit animals', 'Edit categories']);
const keyword = ref('');
let filtered = tasks.value;

const pickTask = (event) => {
  const inputArr = event.target.innerText.split(' ');
  const lowerCase = inputArr.map(el => el.toLowerCase());
  let routeName = '';
  lowerCase.forEach(el => routeName += el + '-')
  routeName = routeName.slice(0, routeName.length - 1);
  router.push(`/admin/${routeName}`);
}

const reset = () => {
  filtered = tasks.value;
  keyword.value = '';
}

onBeforeUpdate(() => {
  /*
  There was a rendering issue using this for @input for the search field.
  So now I'm forcing to update the list just before the render
   */
  if (keyword.value !== '') {
    filtered = tasks.value.filter(el => el.toLowerCase().includes(keyword.value.toLowerCase()));
    return null;
  }
  filtered = tasks.value;
})
</script>
