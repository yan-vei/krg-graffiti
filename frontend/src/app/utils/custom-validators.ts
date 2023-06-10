import { AbstractControl, ValidationErrors, ValidatorFn } from "@angular/forms";

export function indexValidator(): ValidatorFn {
  return (control: AbstractControl) : ValidationErrors | null => {
    const value = control.value;

    if (!value) {
      return null;
    }

    const isNumeric = /[0-9]+/.test(value);

    const indexValid = isNumeric;

    return !indexValid ? {indexNumeric:true} : null;
  }
}

export function coordinatesValidator(): ValidatorFn {
  return (control: AbstractControl) : ValidationErrors | null => {
    const value = control.value;

    if (!value) {
      return null;
    }

    const isNumeric = /[0-9.]+/.test(value);

    const coordinateValid = isNumeric;

    return !coordinateValid ? {coordinateNumeric:true} : null;
  }
}
