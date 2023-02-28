<template>
  <div>
    <div>
      Admin Tools
    </div>

    <AdminAddItem />

    <div class="field">
      <p class="control">
        <button @click="logout" class="button is-success">
          Logout
        </button>
      </p>
    </div>
  </div>
</template>

<script setup>
const loggedIn = useLogin();

const logout = () => {
  loggedIn.value = false;
  sessionStorage.setItem("loggedIn", `${loggedIn.value}`);
}
</script>
