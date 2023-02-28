<template>
  <AdminAddItem />
</template>

<script setup>
const router = useRouter();
const loggedIn = useLogin();

onMounted(() => {
  loggedIn.value = sessionStorage.getItem("loggedIn") === "true";
  if (!loggedIn.value) router.push('/admin');
});

definePageMeta({ layout: "admin-layout" });
</script>

<style scoped>

</style>
