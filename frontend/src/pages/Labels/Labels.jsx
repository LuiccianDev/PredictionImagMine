import React, { useState, useEffect } from "react";
import { getLabels, createLabel } from "../../api/labels";
import LabelForm from "../../components/LabelsForm/LabelsForm"

const Labels = () => {
  const [labels, setLabels] = useState([]);

  useEffect(() => {
    fetchLabels();
  }, []);

  const fetchLabels = async () => {
    const data = await getLabels();
    setLabels(data);
  };

  const handleCreateLabel = async (labelData) => {
    await createLabel(labelData);
    fetchLabels();
  };

  return (
    <div>
      <h1>Etiquetas</h1>
      <LabelForm onSubmit={handleCreateLabel} />
      <ul>
        {labels.map((label) => (
          <li key={label.id}>
            {label.real_label} - {label.feedback ? "Confirmado" : "Pendiente"}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Labels;
