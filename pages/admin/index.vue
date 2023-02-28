<template>
  <div class="container">
    <AdminLogin v-if="!loggedIn"/>
    <AdminPanel v-else/>
  </div>
</template>

<script setup>
const loggedIn = useLogin();

onMounted(() => {
  loggedIn.value = sessionStorage.getItem("loggedIn") === "true";
})

definePageMeta({ layout: "admin-layout" });
</script>

