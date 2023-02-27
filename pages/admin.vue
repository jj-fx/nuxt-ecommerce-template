<template>
  <AdminLogin v-if="!loggedIn"/>
  <AdminPanel v-else/>
</template>

<script setup>
const loggedIn = useLogin();

onMounted(() => {
  loggedIn.value = sessionStorage.getItem("loggedIn") === "true";
})
</script>

