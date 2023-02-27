<template>
  <h1>Home Screen</h1>
  <div>{{ products }}</div>
</template>

<script setup>
const config = useRuntimeConfig().public;
const products = ref('');

onMounted(async () => {
  setTimeout(async () => {
    const { data, error } = await useFetch(`${config.MEDUSA_API}/store/products`);
    products.value = data.value;
  }, 0)
})
</script>
