<template>
  <div>
    <div class="field">
      <div>Add Housing</div>
    </div>
    <div class="field">
      <div>Housing Type</div>
      <label class="checkbox">
        <input type="checkbox">
        Grounded
      </label>
    </div>
    <div class="field">
      <div>Suitable for animals (multiselect):</div>
      <div class="select is-multiple">
        <select multiple size="8">
          <option value="cats">Cats</option>
          <option value="dogs">Dogs</option>
          <option value="birds">Birds</option>
          <option value="elephants">Elephants</option>
        </select>
      </div>
    </div>
    <div class="field">
      <textarea class="textarea" placeholder="Add detailed housing description here..."></textarea>
    </div>
    <div class="field">
      <div>Price (PLN)</div>
      <input class="input" type="number" value="1500">
    </div>
    <div class="field">
      <p class="control">
        <button @click="" class="button is-success">
          Preview
        </button>
      </p>
    </div>
  </div>
</template>
