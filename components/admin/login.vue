<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content">
      <div class="card">
        <div class="card-content">
          <div class="field">
            <p>Limited Access: admin only!</p>
          </div>
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
              <button @click.prevent="login" class="button is-success">
                Login
              </button>
            </p>
          </div>
        </div>
      </div>
    </div>
    <button @click="close" class="modal-close is-large" aria-label="close"></button>
  </div>
</template>

<script setup>
const router = useRouter();
const loggedIn = useLogin();

const email = ref('');
const pwd = ref('');
const adminEmail = ref('admin@email.com');
const adminPwd = ref('admin123');

const close = () => {
  router.push('/');
}

const login = () => {
  if (email.value !== adminEmail.value || pwd.value !== adminPwd.value) {
    console.warn('Access Denied: incorrect email');
    return null;
  }
  loggedIn.value = true;
  sessionStorage.setItem("loggedIn", `${loggedIn.value}`);
}
</script>

<style scoped>

</style>
