<template>
  <h1>Home Screen</h1>
  <div>{{ products }}</div>
</template>

<script setup>
const config = useRuntimeConfig().public;
const products = ref('');

const get = async () => {
  const { data, error } = await useFetch(`${config.MEDUSA_API}/store/products`);
  products.value = data.value;
}

onMounted(async () => {
  setTimeout(async () => {
    await get();
  }, 0)
})
</script>
