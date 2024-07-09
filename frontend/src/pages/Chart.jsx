"use client";
import React, { PureComponent } from "react";
import { PieChart, Pie, Tooltip } from "recharts";

function Chart({ positive, negative }) {
  const data = [
    { name: "Positive", value: positive },
    { name: "Negative", value: negative },
  ];

  return (
    <div>
      <PieChart width={400} height={400}>
        <Pie
          dataKey="value"
          isAnimationActive={false}
          data={data}
          cx="50%"
          cy="50%"
          outerRadius={80}
          fill="#8884d8"
          label
        />
        <Tooltip />
      </PieChart>
    </div>
  );
}

export default Chart;
