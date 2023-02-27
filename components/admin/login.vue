<template>
  <div>
    <div class="field">
      <p class="control has-icons-left has-icons-right">
        <input
            v-model="email"
            class="input"
            type="email"
            placeholder="Email">
        <span class="icon is-small is-left">
      <i class="fas fa-envelope"></i>
    </span>
        <span class="icon is-small is-right">
      <i class="fas fa-check"></i>
    </span>
      </p>
    </div>
    <div class="field">
      <p class="control has-icons-left">
        <input
            v-model="pwd"
            class="input"
            type="password"
            placeholder="Password">
        <span class="icon is-small is-left">
      <i class="fas fa-lock"></i>
    </span>
      </p>
    </div>
    <div class="field">
      <p class="control">
        <button @click="login" class="button is-success">
          Login
        </button>
      </p>
    </div>
  </div>
</template>

<script setup>
const loggedIn = useLogin();

const email = ref('');
const pwd = ref('');
const adminEmail = ref('admin@jas.io');
const adminPwd = ref('admin123');

const login = () => {
  if (email.value !== adminEmail.value || pwd.value !== adminPwd.value) {
    console.log('Access Denied: incorrect email');
    return null;
  }
  loggedIn.value = true;
  sessionStorage.setItem("loggedIn", `${loggedIn.value}`);
}
</script>

<style scoped>

</style>
