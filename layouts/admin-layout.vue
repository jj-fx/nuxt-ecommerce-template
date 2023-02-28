<template>
  <nav class="navbar has-background-grey-light" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-start ml-6">
        <a @click="goTo('/')" class="navbar-item">
          Home
        </a>

        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            Admin Tools
          </a>

          <div class="navbar-dropdown">
            <a @click="goTo('/admin/add-item')" class="navbar-item">
              Add Item
            </a>
            <a @click="goTo('/admin/edit-item')" class="navbar-item">
              Edit Item
            </a>
            <a @click="goTo('/admin/edit-categories')" class="navbar-item">
              Edit Categories
            </a>
            <a @click="goTo('/admin/edit-animals')" class="navbar-item">
              Edit Animals
            </a>
          </div>
        </div>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a v-if="loggedIn" @click="logout" class="button is-warning">
              Log out
            </a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
const router = useRouter();
const loggedIn = useLogin();

const goTo = (route) => {
  router.push(route);
}

const logout = () => {
  loggedIn.value = false;
  sessionStorage.setItem("loggedIn", `${loggedIn.value}`);
  router.push('/admin');
}
</script>
