import React from "react";
import { useSelector } from "react-redux";
import { RootState } from "../../store/store";
import Accordeon from "../ui/Accordeon";

const Photo: React.FC = () => {
  const { data } = useSelector((state: RootState) => state.tour);

  return (
    <Accordeon
      title={<h2 className="pl-10 title-2 smbl:pl-0">Photo</h2>}
      className="pt-30"
    >
      {data.photos?.images.length ? (
        <ul className="pb-20 grid grid-cols-2 gap-[10px] bottom-line tb:grid-cols-1">
          {data.photos?.images.map((photo, key) => (
            <li className="max-h-[295px]" key={key}>
              <img className="w-full h-full object-cover tb:mx-auto" src={`http://${photo}`} alt="minor" />
            </li>
          ))}
        </ul>
      ) : (
        <span>Empty</span>
      )}
    </Accordeon>
  );
};

export default Photo;
