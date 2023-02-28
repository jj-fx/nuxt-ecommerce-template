<template>
  <div class="panel m-6">
    <p class="panel-heading">Add Housing</p>
    <div class="panel-block">
      <label class="checkbox">
        <input type="checkbox">
        Grounded
      </label>
    </div>
    <div class="panel-block">
      <div>
        <div class="m-1">Suitable for animals (multiselect):</div>
        <div class="select is-multiple is-fullwidth">
          <select multiple size="8">
            <option value="cats">Cats</option>
            <option value="dogs">Dogs</option>
            <option value="birds">Birds</option>
            <option value="elephants">Elephants</option>
          </select>
        </div>
      </div>
    </div>
    <div class="panel-block">
      <textarea class="textarea" placeholder="Add detailed housing description here..."></textarea>
    </div>
    <div class="panel-block">
      <div>Price (PLN)</div>
      <input class="input" type="number" value="1500">
    </div>
    <div class="panel-block">
      <p class="control">
        <button @click="" class="button is-success">
          Preview
        </button>
      </p>
    </div>
  </div>
</template>
