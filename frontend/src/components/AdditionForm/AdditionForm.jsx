import React from "react";
import DeviceForm from "../DevicesForm/DevicesForm";
import LocationForm from "../LocationsForm/LocationsForm";
import LabelForm from "../LabelsForm/LabelsForm";

const AdditionalInfoForm = ({ showAskMoreInfo, showForms, handleMoreInfo, handleFormsSubmit, formsCompleted }) => {
  return (
    <div >
      {/* Pregunta si desea agregar más información */}
      {showAskMoreInfo && (
        <div >
          <p>¿Deseas agregar más información?</p>
          <button onClick={() => handleMoreInfo("yes")}>Sí</button>
          <button onClick={() => handleMoreInfo("no")}>No</button>
        </div>
      )}

      {/* Formularios que solo aparecen si el usuario dijo "Sí" */}
      {showForms && !formsCompleted && (
        <div >
          <DeviceForm />py
          <LocationForm />
          <LabelForm />
          <button onClick={handleFormsSubmit}>Confirmar datos</button>
        </div>
      )}
    </div>
  );
};

export default AdditionalInfoForm;
